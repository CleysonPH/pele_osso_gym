from datetime import datetime

from app import db


class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    peso = db.Column(db.Float, nullable=True)
    altura = db.Column(db.Float, nullable=True)
    sexo = db.Column(db.String(1), nullable=False)
    observacoes = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(1), nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False)


    def __init__(
            self, nome=None, email=None, cpf=None, telefone=None, data_nascimento=None,
            peso=None, altura=None, sexo=None, observacoes=None):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.observacoes = observacoes
        self.status = 'A'
        self.data_criacao = datetime.now()


    def __repr__(self):
        return f'<Aluno {self.nome}>'
