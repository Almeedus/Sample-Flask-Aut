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


@app.route("/hello-world", methods =["GET"])
def hello_world():
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)


