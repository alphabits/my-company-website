# coding=utf-8

from wtforms import Form, TextField, validators, PasswordField, ValidationError



class AnswerForm(Form):
    username = TextField('Username', [validators.Length(min=4,max=50),authorize_user])
    password = PasswordField('Password', [validators.Required()])
