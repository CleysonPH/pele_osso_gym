from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required

from app import app
from app.autenticacao.forms import LoginForm
from app.autenticacao.models import User


@app.route('/login/', methods=['GET', 'POST'])
def login():
    titulo = 'Login'
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(usuario=form.usuario.data).first()

        if user is None:
            flash('Nome de Usuario incorreto')
        elif user.verificar_senha(form.senha.data):
            login_user(user)
            flash('Login realizado com sucesso!')

            next = request.args.get('next')

            if next is None or not next[0] == '/':
                next = url_for('home')

            return redirect(next)
        else:
            flash('Senha Incorreta')
    return render_template('autenticacao/login.html', form=form)



@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('Logout realizado com sucesso!')
    return redirect(url_for('login'))
