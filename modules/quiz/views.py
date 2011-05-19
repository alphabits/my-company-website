import os
from flask import Module, url_for, render_template, request, session, redirect

import config
from modules.users.utils import logged_in

from .models import get_questions


quiz = Module(__name__, 'quiz')

@logged_in
@quiz.route('/')
def index():
    questions = get_questions()
    return render_template('quiz/index.html', **locals())
