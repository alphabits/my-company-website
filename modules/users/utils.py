from functools import wraps

from flask import redirect, url_for, session

from .config import USERNAME_KEY, PASSWORD_KEY


def logged_in(view):
    @wraps(view)
    def secret_view():
        if USERNAME_KEY not in session:
            return redirect(url_for('users.login'))
        return view()
    return secret_view
        

