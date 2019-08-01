from flask import render_template, request

from app import app
from app.exercicio.models import Exercicio


@app.route('/listar/exercicio/')
def listar_exercicios():
    titulo = 'Lista de Exercicios'

    busca = request.args.get('q', '')

    exercicios = Exercicio.query.filter(Exercicio.nome.contains(busca)).all()

    return render_template('exercicio/listar_exercicios.html', titulo=titulo, exercicios=exercicios)


@app.route('/cadastrar/exercicio/', methods=['GET', 'POST'])
def cadastrar_exercicio():
    titulo = 'Cadastrar Exercicio'
    exercicio = None

    if request.method == 'GET':
        return render_template('exercicio/formulario_exercicio.html', titulo=titulo, exercicio=exercicio)

    
