# coding=utf-8

from wtforms import Form, TextField, validators, PasswordField


class LoginForm(Form):
    username = TextField('Username', [validators.Length(min=4,max=50)])
    password = PasswordField('Message', [validators.Required()])
