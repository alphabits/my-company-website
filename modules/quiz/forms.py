# coding=utf-8

from wtforms import Form, TextField, TextAreaField, validators, SelectField



class AnswerForm(Form):
    title = TextField('Title', [validators.Length(min=4,max=50)])
    body = TextAreaField('Answer', [validators.Required()])
    language = SelectField('Language', [validators.Required()])

def get_answer_form(request_data, languages_allowed, answer=None):
    form = AnswerForm(request_data, answer)
    form.language.choices = [(l, l.replace('-', ' ').title()) for l in languages_allowed]
    return form
