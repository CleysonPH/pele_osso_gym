from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    usuario = db.Column(db.String(80), unique=True, nullable=False, index=True)
    senha_hash = db.Column(db.String(128))


    def __init__(self, nome, cpf, email, telefone, usuario, senha):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.usuario = usuario
        self.senha_hash = generate_password_hash(senha)


    def __repr__(self):
        return f'<Usuario {self.usuario}>'


    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)
