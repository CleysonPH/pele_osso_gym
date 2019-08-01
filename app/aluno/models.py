from app import db


class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    peso = db.Column(db.Float, nullable=True)
    altura = db.Column(db.Float, nullable=True)
    sexo = db.Column(db.String(1), nullable=True)
    observacoes = db.Column(db.Text, nullable=True)


    def __init__(
            self, nome, email, cpf, telefone, data_nascimento,
            peso, altura, sexo, observacoes):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.peso = peso or None
        self.altura = altura or None
        self.sexo = sexo or None
        self.observacoes = observacoes or None


    def __repr__(self):
        return f'<Aluno {self.nome}>'
