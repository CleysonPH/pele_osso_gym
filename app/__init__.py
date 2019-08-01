from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)


from app.aluno import routes
from app.aluno import models
from app.instrutor import routes
from app.instrutor import models