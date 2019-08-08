from datetime import datetime

from app import db


class Ficha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(1), nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False)

    instrutor_id = db.Column(db.Integer, db.ForeignKey('instrutor.id'), nullable=False)
    instrutor = db.relationship('Instrutor', backref=db.backref('fichas', lazy=True))

    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    aluno = db.relationship('Aluno', backref=db.backref('fichas', lazy=True))


    def __init__(self, nome=None, instrutor=None, aluno=None, data_inicio=None, data_fim=None):
        self.nome = nome
        self.instrutor = instrutor
        self.aluno = aluno
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = 'A'
        self.data_criacao = datetime.now()
    

    def __repr__(self):
        return f'<Ficha {self.nome}>'
