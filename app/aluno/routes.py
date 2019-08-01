from flask import render_template, request, flash, redirect, url_for

from app import app, db
from app.aluno.models import Aluno


@app.route('/listar/alunos/')
def lista_alunos():
    titulo = 'Lista de Alunos'

    busca = request.args.get('q', '')

    alunos = Aluno.query.filter(Aluno.nome.contains(busca)).all()

    return render_template('/aluno/lista_alunos.html', titulo=titulo, alunos=alunos)


@app.route('/cadastrar/aluno/', methods=['GET', 'POST'])
def cadastrar_aluno():
    aluno = None
    titulo = 'Cadastrar Aluno'

    if request.method == 'GET':
        return render_template('/aluno/formulario_aluno.html', titulo=titulo, aluno=aluno)
    
    aluno = Aluno(
        nome = request.form.get('nome'),
        email = request.form.get('email'),
        cpf = request.form.get('cpf'),
        telefone = request.form.get('telefone'),
        data_nascimento = request.form.get('data_nascimento'),
        peso = request.form.get('peso'),
        altura = request.form.get('altura'),
        sexo = request.form.get('sexo'),
        observacoes = request.form.get('observacoes'),
        status = 'A'
    )

    db.session.add(aluno)
    db.session.commit()

    flash('Aluno cadastrado com sucesso!')

    return redirect(url_for('cadastrar_aluno'))


@app.route('/detalhes/aluno/<int:id>/')
def detalhar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    titulo = 'Detalhes do Aluno'

    return render_template('/aluno/detalhar_aluno.html', titulo=titulo, aluno=aluno)


@app.route('/editar/aluno/<int:id>/', methods=['GET', 'POST'])
def editar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    titulo = 'Editar Aluno'

    if request.method == 'GET':
        return render_template('/aluno/formulario_aluno.html', titulo=titulo, aluno=aluno)
    
    aluno.nome = request.form.get('nome')
    aluno.email = request.form.get('email')
    aluno.cpf = request.form.get('cpf')
    aluno.telefone = request.form.get('telefone')
    aluno.data_nascimento = request.form.get('data_nascimento')
    aluno.peso = request.form.get('peso')
    aluno.altura = request.form.get('altura')
    aluno.sexo = request.form.get('sexo')
    aluno.observacoes = request.form.get('observacoes')

    db.session.commit()

    flash('Aluno editado com sucesso!')

    return redirect(url_for('detalhar_aluno', id=aluno.id))


@app.route('/status/aluno/<int:id>')
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