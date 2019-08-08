from datetime import datetime, timedelta
from flask import render_template

from app import app
from app.aluno.models import Aluno
from app.instrutor.models import Instrutor
from app.exercicio.models import Exercicio
from app.ficha.models import Ficha


@app.route('/')
def home():
    titulo = 'Home'

    comparacao = datetime.now() - timedelta(days=7)

    alunos = Aluno.query.filter(Aluno.data_criacao >= comparacao).count()
    instrutores = Instrutor.query.filter(Instrutor.data_criacao >= comparacao).count()
    exercicios = Exercicio.query.filter(Exercicio.data_criacao >= comparacao).count()
    fichas = Ficha.query.filter(Ficha.data_criacao >= comparacao).count()

    return render_template('core/home.html', titulo=titulo, alunos=alunos, instrutores=instrutores, exercicios=exercicios, fichas=fichas)
