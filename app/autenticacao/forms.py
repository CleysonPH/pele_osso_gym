from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')


class AlterarSenhaForm(FlaskForm):
    senha_atual = PasswordField('Senha Atual', validators=[DataRequired()])
    senha_nova = PasswordField('Nova Senha', validators=[DataRequired(), EqualTo('confirmacao', 'Senhas devem ser iguais')])
    confirmacao = PasswordField('Repitir Senha')
    submit = SubmitField('Salvar')
