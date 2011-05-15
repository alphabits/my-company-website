# coding=utf-8

from wtforms import Form, BooleanField, TextField, TextAreaField, validators


class ContactForm(Form):
    name = TextField('Name', [validators.Length(min=4,max=50)])
    email = TextField('Email', [validators.Email()])
    message = TextAreaField('Message', [validators.Required()])
