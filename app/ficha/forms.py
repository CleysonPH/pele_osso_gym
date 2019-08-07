from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from app.instrutor.models import Instrutor
from app.aluno.models import Aluno


def instrutor_query():
    return Instrutor.query.filter(Instrutor.status == 'A')


def aluno_query():
    return Aluno.query.filter(Aluno.status == 'A')


def get_pk(obj):
    return str(obj)


class FichaForm(FlaskForm):
    nome = StringField('Nome da Ficha', validators=[DataRequired()])
    data_inicio = DateField('Data de Inicio', validators=[DataRequired()], format='%d/%m/%Y')
    data_fim = DateField('Data de Finalização', validators=[DataRequired()], format='%d/%m/%Y')
    instrutor = QuerySelectField('Instrutor', validators=[DataRequired()], query_factory=instrutor_query, allow_blank=False, get_pk=get_pk, get_label='nome')
    aluno = QuerySelectField('Aluno', validators=[DataRequired()], query_factory=aluno_query, allow_blank=False, get_pk=get_pk, get_label='nome')
    submit = SubmitField('Salvar')
