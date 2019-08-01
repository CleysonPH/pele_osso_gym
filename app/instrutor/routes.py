from flask import render_template

from app import app
from app.instrutor.models import Instrutor


@app.route('/listar/instrutor/')
def listar_instrutores():
    titulo = 'Lista de Instrutores'
    instrutores = Instrutor.query.all()

    return render_template(
        'instrutor/listar_instrutores.html', titulo=titulo, instrutores=instrutores)