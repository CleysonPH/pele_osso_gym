from flask import render_template, request, redirect, url_for, flash

from app import app, db
from app.treino.models import Treino
from app.exercicio.models import Exercicio
from app.ficha.models import Ficha


@app.route('/ficha/<int:id>/cadastrar/treino/', methods=['GET', 'POST'])
def cadastrar_treino(id):
    ficha = Ficha.query.get_or_404(id)

    titulo = 'Cadastrar Treino'
    treino = None
    exercicios = Exercicio.query.filter(Exercicio.status == 'A')
    
    if request.method == 'GET':
        return render_template('treino/formulario_treino.html', titulo=titulo, treino=treino, exercicios=exercicios)

    treino = Treino(
            exercicio=Exercicio.query.get(request.form.get('exercicio')),
            carga=request.form.get('carga'),
            repeticao=request.form.get('repeticao'),
            secao=request.form.get('secao'),
            descanso=request.form.get('descanso'),
            ficha=Ficha.query.get(id)
    )

    db.session.add(treino)
    db.session.commit()

    flash('Treino Cadastrado com sucesso!')

    return redirect(url_for('detalhar_ficha', id=id))
