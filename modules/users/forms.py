# coding=utf-8

from wtforms import Form, TextField, validators, PasswordField, ValidationError

from .models import authorize, generate_password


def authorize_user(form, field):
    if not authorize(field.data, generate_password(form.password.data)):
        raise ValidationError('Username and/or password not found')

class LoginForm(Form):
    username = TextField('Username', [validators.Length(min=4,max=50),authorize_user])
    password = PasswordField('Password', [validators.Required()])
