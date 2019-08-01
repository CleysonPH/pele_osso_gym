from flask import render_template, request, flash, redirect, url_for

from app import app, db
from app.aluno.models import Aluno


@app.route('/alunos/listar/')
def lista_alunos():
    alunos = Aluno.query.all()

    return render_template('/aluno/lista_alunos.html', alunos=alunos)


@app.route('/aluno/cadastrar/', methods=['GET', 'POST'])
def cadastrar_aluno():
    if request.method == 'GET':
        return render_template('/aluno/cadastar_aluno.html')
    
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
