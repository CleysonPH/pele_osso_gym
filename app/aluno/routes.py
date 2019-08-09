from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required

from app import app, db
from app.aluno.models import Aluno
from app.aluno.forms import AlunoForm


@app.route('/listar/alunos/')
@login_required
def lista_alunos():
    titulo = 'Lista de Alunos'

    busca = request.args.get('q', '')

    alunos = Aluno.query.filter(Aluno.nome.contains(busca)).all()

    return render_template('/aluno/lista_alunos.html', titulo=titulo, alunos=alunos)


@app.route('/cadastrar/aluno/', methods=['GET', 'POST'])
@login_required
def cadastrar_aluno():
    titulo = 'Cadastrar Aluno'
    form = AlunoForm()
    
    if form.validate_on_submit():
        aluno = Aluno()
        form.populate_obj(aluno)

        db.session.add(aluno)
        db.session.commit()

        flash('Aluno cadastrado com sucesso!')

        return redirect(url_for('cadastrar_aluno'))
    return render_template('/aluno/formulario_aluno.html', titulo=titulo, form=form)


@app.route('/detalhes/aluno/<int:id>/')
@login_required
def detalhar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    titulo = 'Detalhes do Aluno'

    return render_template('/aluno/detalhar_aluno.html', titulo=titulo, aluno=aluno)


@app.route('/editar/aluno/<int:id>/', methods=['GET', 'POST'])
@login_required
def editar_aluno(id):
    titulo = 'Editar Aluno'
    aluno = Aluno.query.get_or_404(id)
    form = AlunoForm(obj=aluno)
    
    if form.validate_on_submit():
        form.populate_obj(aluno)

        db.session.commit()

        flash('Aluno editado com sucesso!')

        return redirect(url_for('lista_alunos'))
    return render_template('/aluno/formulario_aluno.html', titulo=titulo, form=form)


@app.route('/status/aluno/<int:id>')
@login_required
def status_aluno(id):
    aluno = Aluno.query.get_or_404(id)

    if aluno.status == 'A':
        aluno.status = 'T'
        db.session.commit()
        flash('Matricula trancada com sucesso!')
    else:
        aluno.status = 'A'
        db.session.commit()
        flash('Matricula destrancada com sucesso!')

    return redirect(url_for('lista_alunos'))