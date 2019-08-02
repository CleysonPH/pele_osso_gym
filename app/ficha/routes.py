from flask import request, render_template

from app import app
from app.ficha.models import Ficha


@app.route('/listar/fichas/')
def listar_fichas():
    titulo = 'Listar Fichas'

    busca = request.args.get('q', '')

    fichas = Ficha.query.filter(Ficha.nome.contains(busca)).all()

    return render_template('ficha/listar_fichas.html', titulo=titulo, fichas=fichas)
