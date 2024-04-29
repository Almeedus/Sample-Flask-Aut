from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY']='your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

#Criação de VIEW Login (rota para verificar login e senha)
login_manager.login_view = "login"

#Função para recuperar o ID do usuário no banco de dados
@login_manager.user_loader
def load_user(user_id):
     return User.query.get(user_id)

@app.route("/login", methods =["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        #Procurar pelo usuário e fazer login
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
                login_user(user)
                print(current_user.is_authenticated)
                return jsonify({"message":"Autenticação realizada com sucesso"}), 200

    return jsonify({"message":"Credenciais inválidas"}), 400


#Para acessar essa rota, precisa estar autenticado anteriormente
@app.route("/logout", methods=["GET"])
@login_required #o decorator login_required faz com que essa rota só seja acessada se autenticado
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso"}), 200


@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        userValidate = User.query.filter_by(username=username).first()

        if userValidate and userValidate.password == password:
             return jsonify({"message":"usuário já existente"}), 409
        
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message":"Usuário cadastrado com sucesso"}), 200
    
    return jsonify({"message":"Dados inválidos"}), 400


@app.route("/user/<int:id_user>", methods=["GET"])
@login_required
def read_user(id_user):
    user = User.query.get(id_user)

    if user:
        return jsonify({"username": user.username})
    
    return jsonify({"message": "Usuário não encontrado"}), 404


@app.route("/user/<int:id_user>", methods=["PUT"])
@login_required
def update_user(id_user):
    data = request.json
    user = User.query.get(id_user)

    if user and data.get("password"):
        user.password = data.get("password")
        db.session.commit()

        return jsonify({"message": f"Usuário {id_user} cadastrado com sucesso"}), 200
    
    return jsonify({"message": "Usuário não encontrado"}), 404


@app.route("/user/<int:id_user>", methods=["DELETE"])
@login_required
def delete_user(id_user):
    user = User.query.get(id_user)

    if id_user == current_user.id:
        return jsonify({"message": "Deleção não permitida"}), 403

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"Usuário {id_user} deletado com sucesso"}), 200
    
    return jsonify({"message": "Usuário não encontrado"}), 404 

@app.route("/hello-world", methods =["GET"])
def hello_world():
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)


