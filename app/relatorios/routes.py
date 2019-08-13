from flask import render_template
from flask_weasyprint import render_pdf, HTML

from app import app
from app.ficha.models import Ficha


@app.route('/ficha_<int:id>.pdf')
def imprimir_ficha(id):
    ficha = Ficha.query.get_or_404(id)
    titulo = f'Ficha {ficha.nome}'

    html = render_template('relatorios/imprimir_ficha.html', titulo=titulo, ficha=ficha)
    return render_pdf(HTML(string=html))
