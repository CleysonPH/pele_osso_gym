from flask import render_template, request, flash, redirect, url_for

from app import app, db
from app.instrutor.models import Instrutor


@app.route('/listar/instrutor/')
def listar_instrutores():
    titulo = 'Lista de Instrutores'
    instrutores = Instrutor.query.all()

    return render_template(
        'instrutor/listar_instrutores.html', titulo=titulo, instrutores=instrutores)


@app.route('/cadastar/instrutor/', methods=['GET', 'POST'])
def cadastrar_instrutor():
    titulo = 'Cadastrar Instrutor'
    instrutor = None;

    if request.method == 'GET':
        return render_template('instrutor/formulario_instrutor.html', titulo=titulo, instrutor=instrutor)

    instrutor = Instrutor(
        nome = request.form.get('nome'),
        email = request.form.get('email'),
        cpf = request.form.get('cpf'),
        telefone = request.form.get('telefone'),
        data_nascimento = request.form.get('data_nascimento'),
        sexo = request.form.get('sexo'),
        faculdade = request.form.get('faculdade'),
        confef_cref = request.form.get('confef_cref'),
        status = 'A',
    )

    db.session.add(instrutor)
    db.session.commit()

    flash('Instrutor cadastrado com sucesso!')

    return redirect(url_for('cadastrar_instrutor'))
