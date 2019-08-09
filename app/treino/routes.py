from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required

from app import app, db
from app.treino.models import Treino
from app.ficha.models import Ficha
from app.treino.forms import TreinoForm


@app.route('/ficha/<int:id>/cadastrar/treino/', methods=['GET', 'POST'])
@login_required
def cadastrar_treino(id):
    titulo = 'Cadastrar Treino'
    form = TreinoForm()
    ficha = Ficha.query.get_or_404(id)

    if form.validate_on_submit():
        treino = Treino()
        form.populate_obj(treino)
        treino.ficha = ficha 
        
        db.session.add(treino)
        db.session.commit()
        
        flash('Treino cadastrado com sucesso!')
        
        return redirect(url_for('detalhar_ficha', id=ficha.id))
    return render_template('treino/formulario_treino.html', titulo=titulo, form=form)
        
        
@app.route('/editar/treino/<int:id>/', methods=['GET', 'POST'])
@login_required
def editar_treino(id):
    titulo = 'Editar Treino'
    treino = Treino.query.get_or_404(id)
    form = TreinoForm(obj=treino)

    if form.validate_on_submit():
        form.populate_obj(treino)
        
        db.session.commit()
        
        flash('Treino editado com sucesso!')
        
        return redirect(url_for('detalhar_ficha', id=treino.ficha.id))
    return render_template('treino/formulario_treino.html', titulo=titulo, form=form)


@app.route('/apagar/treino/<int:id>')
@login_required
def apagar_treino(id):
    treino = Treino.query.get_or_404(id)
    ficha_id = treino.ficha.id

    db.session.delete(treino)
    db.session.commit()

    flash('Treino deletado com sucesso!')

    return redirect(url_for('detalhar_ficha', id=ficha_id))
