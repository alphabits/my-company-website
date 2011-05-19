import os
from flask import Module, url_for, render_template, request, session, redirect, g

import config
from app import app

from .models import User, authorize, generate_password
from .forms import LoginForm
from .config import USERNAME_KEY, PASSWORD_KEY

unk = USERNAME_KEY
pwk = PASSWORD_KEY

users = Module(__name__, 'users')

@app.before_request
def add_user_to_global():
    if unk in session and pwk in session:
        user = authorize(session[unk], session[pwk])
        if user:
            g.user = user


@users.route('/login', methods=["POST", "GET"])
def login():
    if unk in session and pwk in session:
        if authorize(session[unk], session[pwk]):
            return redirect(url_for('quiz.index'))

    login_form = LoginForm(request.form)
    if request.method == "POST" and login_form.validate():
        password = generate_password(login_form.password.data)
        username = login_form.username.data
        if authorize(username, password):
            session[unk] = username
            session[pwk] = password
            return redirect(url_for('quiz.index'))
    return render_template('users/login.html', form=login_form)


@users.route('/logout')
def logout():
    del session[unk]
    del session[pwk]
    return redirect(url_for('users.login'))
