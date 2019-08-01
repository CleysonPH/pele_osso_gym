from flask import render_template, request, flash, redirect, url_for

from app import app, db
from app.instrutor.models import Instrutor


@app.route('/listar/instrutor/')
def listar_instrutores():
    titulo = 'Lista de Instrutores'

    busca = request.args.get('q', '')

    instrutores = Instrutor.query.filter(Instrutor.nome.contains(busca)).all()

    return render_template('instrutor/listar_instrutores.html', titulo=titulo, instrutores=instrutores)


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


@app.route('/detalhes/instrutor/<int:id>')
def detalhar_instrutor(id):
    titulo = 'Detalhes do Instrutor'
    instrutor = Instrutor.query.get_or_404(id)

    return render_template('instrutor/detalhar_instrutor.html', titulo=titulo, instrutor=instrutor)


@app.route('/editar/instrutor/<int:id>', methods=['GET', 'POST'])
def editar_instrutor(id):
    titulo = 'Editar Instrutor'
    instrutor = Instrutor.query.get_or_404(id)

    if request.method == 'GET':
        return render_template('instrutor/formulario_instrutor.html', titulo=titulo, instrutor=instrutor)

    instrutor.nome = request.form.get('nome')
    instrutor.email = request.form.get('email')
    instrutor.cpf = request.form.get('cpf')
    instrutor.telefone = request.form.get('telefone')
    instrutor.data_nascimento = request.form.get('data_nascimento')
    instrutor.sexo = request.form.get('sexo')
    instrutor.faculdade = request.form.get('faculdade')
    instrutor.confef_cref = request.form.get('confef_cref')

    db.session.commit()

    flash('Instrutor editado com sucesso!')

    return redirect(url_for('detalhar_instrutor', id=instrutor.id))


@app.route('/ferias/instrutor/<int:id>/')
def ferias_instrutor(id):
    instrutor = Instrutor.query.get_or_404(id)

    if instrutor.status == 'D':
        flash('O instrutor já está desligado.')
    elif instrutor.status == 'A':
        instrutor.status = 'F'
        db.session.commit()
        flash('Férias dadas com sucesso.')
    else:
        instrutor.status = 'A'
        db.session.commit()
        flash('Férias finalizadas com sucesso.')

    return redirect(url_for('listar_instrutores'))


@app.route('/rh/instrutor/<int:id>/')
def rh_instrutor(id):
    instrutor = Instrutor.query.get_or_404(id)

    if instrutor.status == 'F':
        flash('O instrutor está de férias.')
    elif instrutor.status == 'A':
        instrutor.status = 'D'
        db.session.commit()
        flash('Instrutor desligado com sucesso.')
    else:
        instrutor.status = 'A'
        db.session.commit()
        flash('Instrutor recontratado com sucesso.')

    return redirect(url_for('listar_instrutores'))