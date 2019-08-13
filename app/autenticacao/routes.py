from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user

from app import app, db
from app.autenticacao.forms import LoginForm, AlterarSenhaForm, AlterarDadosForm
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
            lembrar = form.lembrar.data
            login_user(user, remember=lembrar)
            flash('Login realizado com sucesso!')

            next = request.args.get('next')

            if next is None or not next[0] == '/':
                next = url_for('home')

            return redirect(next)
        else:
            flash('Senha Incorreta')
    return render_template('autenticacao/login.html', form=form)


@app.route('/alterar/senha/', methods=['GET', 'POST'])
def alterar_senha():
    usuario = current_user
    titulo = 'Alterar Senha'
    form = AlterarSenhaForm()

    if form.validate_on_submit():
        if usuario.alterar_senha(form.senha_atual.data, form.senha_nova.data):
            db.session.commit()
            
            flash('Senha alterada com sucesso!')
            
            return redirect(url_for('home'))
        
        flash('Senha atual incorreta')
        return redirect(url_for('alterar_senha'))
    return render_template('autenticacao/alterar_senha.html', titulo=titulo, form=form)


@app.route('/alterar/dados/', methods=['GET', 'POST'])
def alterar_dados():
    usuario = current_user
    titulo = 'Atualizar Dados'
    form = AlterarDadosForm(obj=usuario)

    if form.validate_on_submit():
        form.populate_obj(usuario)

        db.session.commit()

        flash('Dados atualizados com sucesso!')

        return redirect(url_for('alterar_dados'))
    return render_template('autenticacao/alterar_dados.html', titulo=titulo, form=form)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('Logout realizado com sucesso!')
    return redirect(url_for('login'))
