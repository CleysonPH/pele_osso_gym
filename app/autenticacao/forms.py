from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, URL, Email, Optional, ValidationError


class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    lembrar = BooleanField('Lembrar de mim', validators=[Optional()])
    submit = SubmitField('Entrar')


class AlterarSenhaForm(FlaskForm):
    senha_atual = PasswordField('Senha Atual', validators=[DataRequired()])
    senha_nova = PasswordField('Nova Senha', validators=[DataRequired(), EqualTo('confirmacao', 'Senhas devem ser iguais')])
    confirmacao = PasswordField('Repitir Senha')
    submit = SubmitField('Salvar')


class AlterarDadosForm(FlaskForm):
    nome = StringField('Nome Completo', validators=[DataRequired()])
    img_url = StringField('Imagem de Perfil', validators=[DataRequired(), URL()])
    cpf = StringField('CPF', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    submit = SubmitField('Salvar')

    def validate_cpf(form, field):
        from validate_docbr import CPF

        cpf = CPF()

        if not cpf.validate(field.data):
            raise ValidationError("CPF Invalido")
