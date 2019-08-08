from datetime import datetime

from app import db


class Exercicio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(1), nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False)


    def __init__(self, nome=None, descricao=None):
        self.nome = nome
        self.descricao = descricao
        self.status = 'A'
        self.data_criacao = datetime.now()


    def __repr__(self):
        return f'<Exercicio {self.nome}>'
