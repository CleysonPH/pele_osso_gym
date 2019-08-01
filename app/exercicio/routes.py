from flask import render_template, request, flash, redirect, url_for

from app import app, db
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

    exercicio = Exercicio(
        nome = request.form.get('nome'),
        descricao = request.form.get('descricao'),
        status = 'A',
    )

    db.session.add(exercicio)
    db.session.commit()

    flash('Exercicio cadastrado com sucesso!')

    return redirect(url_for('cadastrar_exercicio'))
