import os
from flask import Module, url_for, render_template, request, session, redirect, g

import config
from app import app

from .models import User, authorize, generate_password, anonymous
from .forms import LoginForm
from .config import USERNAME_KEY, PASSWORD_KEY
from .utils import user_authorized, get_current_user, logout_current_user, login_user



users = Module(__name__, 'users')

@app.before_request
def add_user_to_global():
    if user_authorized():
        g.user = get_current_user()
    else:
        g.user = anonymous


@users.route('/login', methods=["POST", "GET"])
def login():
    if user_authorized():
        return redirect(url_for('quiz.index'))

    login_form = LoginForm(request.form)
    if request.method == "POST" and login_form.validate():
        password = generate_password(login_form.password.data)
        username = login_form.username.data
        if authorize(username, password):
            login_user(username, password)
            return redirect(url_for('quiz.index'))
    return render_template('users/login.html', form=login_form)


@users.route('/logout')
def logout():
    logout_current_user()
    return redirect(url_for('users.login'))
