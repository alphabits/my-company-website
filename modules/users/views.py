import os
from flask import Module, url_for, render_template, request, session, redirect

import config

from .models import User
from .forms import LoginForm


users = Module(__name__, 'users')


@users.route('/login', methods=["POST", "GET"])
def login():
    if 'username' in session:
        return redirect(url_for('quiz.index'))
    login_form = LoginForm(request.form)
    if request.method == "POST" and login_form.validate():
        session['username'] = True
        return redirect(url_for('quiz.index'))
    return render_template('users/login.html', form=login_form)

@users.route('/logout')
def logout():
    del session["username"]
    return redirect(url_for('users.login'))
