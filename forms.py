# coding=utf-8

from wtforms import Form, BooleanField, TextField, TextAreaField, validators


class ContactForm(Form):
    name = TextField('Name', [validators.Length(min=4,max=50)])
    email = TextField('Email', [validators.Length(min=5,max=120),validators.Email(message=u'Er du sikker på at det er en emailadresse?')])
    message = TextAreaField('Message', [validators.Required()])
