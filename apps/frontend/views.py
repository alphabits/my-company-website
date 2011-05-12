from flask import Module, render_template, url_for, redirect


frontend = Module(__name__, 'frontend')

@frontend.route('/')
def index():
    return redirect(url_for('blog.index'))

@frontend.route('/<any("about"):page>')
def show_page(page):
    return render_template('frontend/%s.html' % (page,))
