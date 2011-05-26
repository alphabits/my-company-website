import os
from flask import Module, url_for, render_template, request, session, redirect,\
        abort, g

import config
from modules.users.utils import logged_in

from .models import Question, Answer
from .forms import get_answer_form


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
    form = get_answer_form(request.form, q.get_languages_allowed())
    
    if request.method == "POST":
        success = False
        if request.form.has_key("open_question"):
            q.open_for_user(g.user)
            q.save()
            success = True
        if form.validate():
            answer = Answer(title=form.title.data, body=form.body.data, 
                    question=q, user=g.user, language=form.language.data)
            answer.save()
            success = True
        if success:
            return redirect(url_for('quiz.show_question', id=q.id))
    
    answers = Answer.from_user_and_question(g.user, q)

    return render_template('quiz/show-question.html', **locals())

@logged_in
@quiz.route('/questions/<question_id>/answers/<int:answer_id>', methods=["POST","GET"])
def edit_answer(question_id, answer_id):
    q = Question.query.get(question_id)
    a = Answer.query.get(answer_id)
    if q is None or a is None or a.question != q:
        abort(404)
    if a.user != g.user:
        abort(400)
    form = get_answer_form(request.form, q.get_languages_allowed(), a)
    if request.method == "POST" and form.validate():
        a.title = form.title.data
        a.body = form.body.data
        a.language = form.language.data
        a.save()
        return redirect(url_for('quiz.show_question', id=q.id))

    return render_template('quiz/edit-answer.html', **locals())


