from flask import Module, request, render_template, url_for, redirect

from forms import ContactForm


frontend = Module(__name__, 'frontend')



@frontend.route('/')
def index():
    return render_template('frontend/index.html')



_page_route_string = '''
    /<any("about","websites","webapplications","data-analysis",
            "solutions","craftmanship","buzzwords","open-source-tools",
            "who-am-i"):page>
'''.replace(' ', '').replace('\n', '')

@frontend.route(_page_route_string)
def show_page(page):
    return render_template('frontend/%s.html' % (page,))


@frontend.route('/contact', methods=['get','post'])
def contact():
    contact_form = ContactForm(request.form)
    if request.method=="POST" and contact_form.validate():
        return redirect(url_for('frontend.index'))
    return render_template('frontend/contact.html', form=contact_form)

