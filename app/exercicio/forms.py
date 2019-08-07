from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ExercicioForm(FlaskForm):
    nome = StringField('Nome do Exercico', validators=[DataRequired()])
    descricao = TextAreaField('Descrição', validators=[DataRequired()])
    submit = SubmitField('Salvar')
