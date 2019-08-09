from flask import request, render_template, flash, redirect, url_for
from flask_login import login_required

from app import app, db
from app.ficha.models import Ficha
from app.ficha.forms import FichaForm


@app.route('/listar/fichas/')
@login_required
def listar_fichas():
    titulo = 'Listar Fichas'

    busca = request.args.get('q', '')

    fichas = Ficha.query.filter(Ficha.nome.contains(busca)).all()

    return render_template('ficha/listar_fichas.html', titulo=titulo, fichas=fichas)


@app.route('/cadastrar/ficha/', methods=['GET', 'POST'])
@login_required
def cadastrar_ficha():
    titulo = 'Cadastrar Ficha'
    form = FichaForm()

    if form.validate_on_submit():
        ficha = Ficha()
        form.populate_obj(ficha)

        db.session.add(ficha)
        db.session.commit()

        flash('Ficha cadastrada com sucesso!')    

        return redirect(url_for('detalhar_ficha', id=ficha.id))
    return render_template('ficha/formulario_ficha.html', titulo=titulo, form=form)


@app.route('/detalhar/ficha/<int:id>/')
@login_required
def detalhar_ficha(id):
    ficha = Ficha.query.get_or_404(id)
    titulo = 'Detalhes da Ficha'

    return render_template('ficha/detalhar_ficha.html', titulo=titulo, ficha=ficha)


@app.route('/editar/ficha/<int:id>/', methods=['GET', 'POST'])
@login_required
def editar_ficha(id):
    titulo = 'Cadastrar Ficha'
    ficha = Ficha.query.get_or_404(id)
    form = FichaForm(obj=ficha)

    if form.validate_on_submit():
        form.populate_obj(ficha)

        db.session.commit()

        flash('Ficha editada com sucesso!')

        return redirect(url_for('listar_fichas', id=ficha.id))
    return render_template('ficha/formulario_ficha.html', titulo=titulo, form=form)


@app.route('/conclusao/ficha/<int:id>/')
@login_required
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
@login_required
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
