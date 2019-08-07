from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email


class InstrutorForm(FlaskForm):
    nome = StringField('Nome Completo', validators=[DataRequired()])
    email = StringField('Endereço de email', validators=[DataRequired(), Email()])
    telefone = StringField('Telefone para contato', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    data_nascimento = DateField('Data de Nascimento', validators=[DataRequired()], format='%d/%m/%Y')
    sexo = SelectField(
        'Sexo',
        choices=[('F', 'Feminino'), ('M', 'Masculino'), ('X', 'Prefere não informar')]
    )
    faculdade = StringField('Faculdade', validators=[DataRequired()])
    confef_cref = StringField('CONFEF | CREF', validators=[DataRequired()])
    submit = SubmitField('Salvar')
