from flask import render_template, request, flash, redirect, url_for

from app import app, db
from app.exercicio.models import Exercicio
from app.exercicio.forms import ExercicioForm


@app.route('/listar/exercicio/')
def listar_exercicios():
    titulo = 'Lista de Exercicios'

    busca = request.args.get('q', '')

    exercicios = Exercicio.query.filter(Exercicio.nome.contains(busca)).all()

    return render_template('exercicio/listar_exercicios.html', titulo=titulo, exercicios=exercicios)


@app.route('/cadastrar/exercicio/', methods=['GET', 'POST'])
def cadastrar_exercicio():
    titulo = 'Cadastrar Exercicio'
    form = ExercicioForm()

    if form.validate_on_submit():
        exercicio = Exercicio()
        form.populate_obj(exercicio)

        db.session.add(exercicio)
        db.session.commit()

        flash('Exercicio cadastrado com sucesso!')

        return redirect(url_for('cadastrar_exercicio'))
    return render_template('exercicio/formulario_exercicio.html', titulo=titulo, form=form)


@app.route('/detalhes/exercicio/<int:id>')
def detalhar_exercicio(id):
    titulo = 'Detalhes do Exercicio'
    exercicio = Exercicio.query.get_or_404(id)

    return render_template('exercicio/detalhar_exercicio.html', titulo=titulo, exercicio=exercicio)


@app.route('/editar/exercicio/<int:id>', methods=['GET', 'POST'])
def editar_exercicio(id):
    titulo = 'Editar Exercicio'
    exercicio = Exercicio.query.get_or_404(id)
    form = ExercicioForm(obj=exercicio)

    if form.validate_on_submit():
        form.populate_obj(exercicio)

        db.session.commit()

        flash('Exercicio editado com sucesso!')

        return redirect(url_for('listar_exercicios'))
    return render_template('exercicio/formulario_exercicio.html', titulo=titulo, form=form)


@app.route('/manutencao/exercicio/<int:id>')
def manutencao_exercicio(id):
    exercicio = Exercicio.query.get_or_404(id)

    if exercicio.status in 'AI' :
        exercicio.status = 'M'
        db.session.commit()
        flash('Exercicio colocado em manutenção com sucesso!')
    else:
        exercicio.status = 'A'
        db.session.commit()
        flash('Exercicio retirado da manutenção com sucesso!')

    return redirect(url_for('listar_exercicios'))


@app.route('/controlar/status/exercicio/<int:id>')
def desativar_reativar_exercicio(id):
    exercicio = Exercicio.query.get_or_404(id)

    if exercicio.status in 'AM' :
        exercicio.status = 'I'
        db.session.commit()
        flash('Exercicio desativado com sucesso!')
    else:
        exercicio.status = 'A'
        db.session.commit()
        flash('Exercicio reativado com sucesso!')

    return redirect(url_for('listar_exercicios'))
