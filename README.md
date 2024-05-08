# Sample Flask Aut

Este projeto é uma API em Flask para realizar um CRUD de um usuário em uma plataforma de login.

A ideia desse projeto foi retirada do curso de Python intermediario que está disponível na [Rocketseat](https://app.rocketseat.com.br/journey/python/overview).

## 🚀 Começando

Para rodar o projeto basta dar um git clone em sua maquina, para ter uma cópia no seu repositório local.
```
git clone https://github.com/Almeedus/sample-flask-aut.git
```

### 📋 Pré-requisitos

Python 3.12.2
Docker 20.10.24
Docker-compose 1.29.2

### 🔧 Instalação

Com o python3 instalado localmente em sua maquina, abra o diretório do projeto e baixe as bibliotecas que são obrigatórias para o funcionamento do projeto. Para isso siga o seguinte comando.
```
pip3 install -r requirements.txt
```

Após a instalação de todos os requisitos obrigatórios para o projeto, rode o docker-compose para iniciar o container do MySQL:

Atenção: para realizar o comando a seguir, certifique-se de estar no diretório do projeto, pois o comando irá buscar pelo docker-compose.yml
```
docker-compose up
```

Para configurar o banco de dados iremos utilizar o comando do terminal do flask
```
flask shell
```

Dentro do flask shell seguiremos com os seguintes comandos para criar o banco de dados
```
db.create_all()
```

E por fim salvar as mudanças realizadas anteriormente
```
db.session.commit()
```

Pronto, agora é só sair do terminal do flask
```
exit()
```

## ⚙️ Executando os testes

Inicie o módulo criado com o comando
```
python3 app.py
```

### 🔩 Analise os testes de ponta a ponta

Configure os endpoints em seu software de consumo de API de preferencia. 



## 🛠️ Construído com

* [Python](https://docs.python.org/3/) - Linguagem utilizada
* [Flask](https://docs.python.org/3/) - Framework utilizado
* [Docker](https://docs.docker.com/) - Usado para gerar o container de MySQL
* [MySQL](https://dev.mysql.com/doc/) - Banco de Dados utilizado
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/) - Extensão para o FLask para dar suporte ao SQL na aplicação.
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/) - Usada para gerenciar a seção do usuário
* [Werkzeug](https://werkzeug.palletsprojects.com/en/3.0.x/) - Biblioteca abrangente de aplicativos da web WSGI.
* [Pymysql](https://pymysql.readthedocs.io/en/latest/) - Usado para criar o banco de dados.
* [Cryptography](https://cryptography.io/en/latest/) - Usado para criptografia de senhas.


## ✒️ Autores


* **Um desenvolvedor** - *Trabalho Inicial* - [umdesenvolvedor](https://github.com/linkParaPerfil)
* **Fulano De Tal** - *Documentação* - [fulanodetal](https://github.com/linkParaPerfil)

Você também pode ver a lista de todos os [colaboradores](https://github.com/usuario/projeto/colaboradores) que participaram deste projeto.


## 🎁 Expressões de gratidão

* Conte a outras pessoas sobre este projeto 📢;
* Convide alguém da equipe para uma cerveja 🍺;
* Um agradecimento publicamente 🫂;
* etc.


---
⌨️ com ❤️ por [Armstrong Lohãns](https://gist.github.com/lohhans) 😊