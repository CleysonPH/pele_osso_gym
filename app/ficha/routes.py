from flask import request, render_template, flash, redirect, url_for

from app import app, db
from app.ficha.models import Ficha
from app.instrutor.models import Instrutor
from app.aluno.models import Aluno
from app.utils import get_date_from_string


@app.route('/listar/fichas/')
def listar_fichas():
    titulo = 'Listar Fichas'

    busca = request.args.get('q', '')

    fichas = Ficha.query.filter(Ficha.nome.contains(busca)).all()

    return render_template('ficha/listar_fichas.html', titulo=titulo, fichas=fichas)


@app.route('/cadastrar/ficha/', methods=['GET', 'POST'])
def cadastrar_ficha():
    titulo = 'Cadastrar Ficha'
    ficha = None
    instrutores = Instrutor.query.filter(Instrutor.status == 'A')
    alunos = Aluno.query.filter(Aluno.status == 'A')

    if request.method == 'GET':
        return render_template(
            'ficha/formulario_ficha.html',
            titulo=titulo,
            ficha=ficha,
            instrutores=instrutores,
            alunos=alunos
        )

    ficha = Ficha(
        nome = request.form.get('nome'),
        instrutor = Instrutor.query.get(request.form.get('instrutor')),
        aluno = Aluno.query.get(request.form.get('aluno')),
        data_inicio = get_date_from_string(request.form.get('data_inicio')),
        data_fim = get_date_from_string(request.form.get('data_fim')),
    )

    db.session.add(ficha)
    db.session.commit()

    flash('Ficha cadastrada com sucesso!')    

    return redirect(url_for('listar_fichas'))
