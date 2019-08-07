from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Optional

from app.exercicio.models import Exercicio


def exercicio_query():
    return Exercicio.query.filter(Exercicio.status == 'A')


def get_pk(obj):
    return str(obj.id)


class TreinoForm(FlaskForm):
    exercicio = QuerySelectField('Exercicio', validators=[DataRequired()], query_factory=exercicio_query, allow_blank=False, get_pk=get_pk, get_label='nome')
    carga = FloatField('Carga', validators=[Optional()])
    repeticao = IntegerField('Repetição', validators=[Optional()])
    secao = IntegerField('Seção', validators=[Optional()])
    descanso = IntegerField('Descanso', validators=[Optional()])
    submit = SubmitField('Salvar')
