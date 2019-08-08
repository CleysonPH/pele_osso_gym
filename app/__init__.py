from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)


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
