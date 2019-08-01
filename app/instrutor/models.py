from app import db


class Instrutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    faculdade = db.Column(db.String(80), nullable=False)
    confef_cref = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(1), nullable=False)


    def __init__(
            self, nome, email, cpf, telefone, data_nascimento,
            sexo, faculdade, confef_cref, status):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.faculdade = faculdade
        self.confef_cref = confef_cref
        self.status = status


    def __repr__(self):
        return f'<Instrutor {self.nome}>'
