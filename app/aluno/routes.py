from flask import render_template, request, flash, redirect, url_for

from app import app, db
from app.aluno.models import Aluno


@app.route('/listar/alunos/')
def lista_alunos():
    titulo = 'Listar Alunos'
    alunos = Aluno.query.all()

    return render_template('/aluno/lista_alunos.html', titulo=titulo, alunos=alunos)


@app.route('/cadastrar/aluno/', methods=['GET', 'POST'])
def cadastrar_aluno():
    titulo = 'Cadastrar Aluno'

    if request.method == 'GET':
        return render_template('/aluno/cadastar_aluno.html', titulo=titulo)
    
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
    )

    db.session.add(aluno)
    db.session.commit()

    flash('Aluno cadastrado com sucesso!')

    return redirect(url_for('cadastrar_aluno'))


@app.route('/detalhes/aluno/<int:id>')
def detalhar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    titulo = 'Detalhes do Aluno'

    return render_template('/aluno/detalhar_aluno.html', titulo=titulo, aluno=aluno)
