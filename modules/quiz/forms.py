# coding=utf-8

from wtforms import Form, TextField, TextAreaField, validators



class AnswerForm(Form):
    title = TextField('Title', [validators.Length(min=4,max=50)])
    body = TextAreaField('Answer', [validators.Required()])
