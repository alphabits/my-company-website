import os
from flask import Module, url_for, render_template, request, session, redirect,\
        abort, g

import config
from modules.users.utils import logged_in

from .models import Question, Answer
from .forms import AnswerForm


quiz = Module(__name__, 'quiz')


@quiz.route('/')
@logged_in
def index():
    questions = Question.query.all()
    return render_template('quiz/index.html', **locals())

@logged_in
@quiz.route('/questions/<id>', methods=["POST", "GET"])
def show_question(id):
    q = Question.query.filter(Question.id == id).all()
    if not q:
        abort(404)
    q = q[0]
    form = AnswerForm(request.form)
    
    if request.method == "POST":
        success = False
        if request.form.has_key("open_question"):
            q.open()
            q.save()
            success = True
        if form.validate():
            answer = Answer(title=form.title.data, body=form.body.data, 
                    question=q, user=g.user)
            answer.save()
            success = True
        if success:
            return redirect(url_for('quiz.show_question', id=q.id))
    
    answers = Answer.from_user_and_question(g.user, q)

    return render_template('quiz/show-question.html', **locals())
