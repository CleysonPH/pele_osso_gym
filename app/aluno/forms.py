from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SelectField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, Optional


class AlunoForm(FlaskForm):
    nome = StringField('Nome Completo', validators=[DataRequired()])
    email = StringField('Endereço de email', validators=[DataRequired(), Email()])
    telefone = StringField('Telefone para contato', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    data_nascimento = DateField('Data de Nascimento', validators=[DataRequired()], format='%d/%m/%Y')
    peso = FloatField('Peso', validators=[Optional()])
    altura = FloatField('Altura', validators=[Optional()])
    sexo = SelectField(
        'Sexo',
        choices=[('F', 'Feminino'), ('M', 'Masculino'), ('X', 'Prefere não informar')]
    )
    observacoes = TextAreaField('Observações', validators=[Optional()])
    submit = SubmitField('Salvar')


    def validate_cpf(form, field):
        from validate_docbr import CPF

        cpf = CPF()

        if not cpf.validate(field.data):
            raise ValidationError("CPF Invalido")
