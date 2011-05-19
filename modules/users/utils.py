from functools import wraps

from flask import redirect, url_for, session


def logged_in(view):
    @wraps(view)
    def secret_view():
        if 'username' not in session:
            return redirect(url_for('users.login'))
        return view()
    return secret_view
        

