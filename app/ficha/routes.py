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

    return redirect(url_for('detalhar_ficha', id=ficha.id))


@app.route('/detalhar/ficha/<int:id>/')
def detalhar_ficha(id):
    ficha = Ficha.query.get_or_404(id)
    titulo = 'Detalhes da Ficha'

    return render_template('ficha/detalhar_ficha.html', titulo=titulo, ficha=ficha)


@app.route('/editar/ficha/<int:id>/', methods=['GET', 'POST'])
def editar_ficha(id):
    titulo = 'Editar Ficha'
    ficha = Ficha.query.get_or_404(id)
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

    ficha.nome = request.form.get('nome')
    ficha.instrutor = Instrutor.query.get(request.form.get('instrutor'))
    ficha.aluno = Aluno.query.get(request.form.get('aluno'))
    ficha.data_inicio = get_date_from_string(request.form.get('data_inicio'))
    ficha.data_fim = get_date_from_string(request.form.get('data_fim'))

    db.session.commit()

    flash('Ficha editada com sucesso!')

    return redirect(url_for('listar_fichas'))


@app.route('/conclusao/ficha/<int:id>/')
def conclusao_ficha(id):
    ficha = Ficha.query.get_or_404(id)

    if ficha.status == 'A':
        ficha.status = 'C'
        db.session.commit()
        flash('Ficha concluida com sucesso!')
    elif ficha.status == 'C':
        ficha.status = 'A'
        db.session.commit()
        flash('Ficha reativada com sucesso!')
    else:
        flash('A ficha está com o status suspenso!')


    return redirect(url_for('listar_fichas'))


@app.route('/suspensao/ficha/<int:id>/')
def suspensao_ficha(id):
    ficha = Ficha.query.get_or_404(id)

    if ficha.status == 'A':
        ficha.status = 'S'
        db.session.commit()
        flash('Ficha suspensa com sucesso!')
    elif ficha.status == 'S':
        ficha.status = 'A'
        db.session.commit()
        flash('Ficha reativada com sucesso!')
    else:
        flash('A ficha está com o status concluido!')


    return redirect(url_for('listar_fichas'))
