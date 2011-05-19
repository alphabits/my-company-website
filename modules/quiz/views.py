import os
from flask import Module, url_for, render_template, request, session, redirect

import config
from modules.users.utils import logged_in

from .models import get_questions, get_question_by_id


quiz = Module(__name__, 'quiz')

@quiz.route('/')
@logged_in
def index():
    questions = get_questions()
    return render_template('quiz/index.html', **locals())

@logged_in
@quiz.route('/questions/<id>')
def show_question(id):
    q = get_question_by_id(id)
    return render_template('quiz/show-question.html', **locals())
