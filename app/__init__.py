from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


from app.core import routes
from app.aluno import routes
from app.aluno import models
from app.instrutor import routes
from app.instrutor import models
from app.exercicio import routes
from app.exercicio import models
from app.ficha import models
from app.ficha import routes
from app.treino import models
from app.treino import routes
from app.autenticacao import models
from app.autenticacao import routes
