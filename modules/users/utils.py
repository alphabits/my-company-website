from functools import wraps

from flask import redirect, url_for, session, g

from .config import USERNAME_KEY, PASSWORD_KEY
from .models import authorize, User

unk = USERNAME_KEY
pwk = PASSWORD_KEY

def logged_in(view):
    @wraps(view)
    def secret_view():
        if not user_authorized():
            return redirect(url_for('users.login'))
        return view()
    return secret_view
        
def user_authorized():
    return ( unk in session and pwk in session and 
             authorize(session[unk], session[pwk]) )

def get_current_user():
    return User.query.filter(User.username==session[unk]).one()

def logout_current_user():
    del session[unk]
    del session[pwk]
    return True

def login_user(username, password):
    session[unk] = username
    session[pwk] = password
