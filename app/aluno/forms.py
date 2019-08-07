from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class AlunoForm(FlaskForm):
    nome = StringField('Nome Completo', validators=[DataRequired()])
    email = StringField('Endereço de email', validators=[DataRequired(), Email()])
    telefone = StringField('Telefone para contato', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    data_nascimento = DateField('Data de Nascimento', validators=[DataRequired()], format='%d/%m/%Y')
    peso = FloatField('Peso', validators=[DataRequired()])
    altura = FloatField('Altura', validators=[DataRequired()])
    sexo = SelectField(
        'Sexo',
        choices=[('F', 'Feminino'), ('M', 'Masculino'), ('X', 'Prefere não informar')]
    )
    observacoes = TextAreaField('Observações', validators=[DataRequired()])
    submit = SubmitField('Salvar')
