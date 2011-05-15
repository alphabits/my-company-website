from flask import Module, request, render_template, url_for, redirect

from forms import ContactForm


frontend = Module(__name__, 'frontend')



@frontend.route('/')
def index():
    return render_template('frontend/index.html')



pages = [
    'about', 'websites', 'web-application', 'data-analysis',
    'solutions', 'open-source-tools', 'who-am-i'
]
_page_route_string = '/<any(%s):page>' % (','.join(['"%s"'%(p,) for p in pages]))

@frontend.route(_page_route_string)
def show_page(page):
    return render_template('frontend/%s.html' % (page,))


@frontend.route('/contact', methods=['get','post'])
def contact():
    contact_form = ContactForm(request.form)
    if request.method=="POST" and contact_form.validate():
        return render_template('frontend/contact_success.html', 
                name=request.form['name'])
    return render_template('frontend/contact.html', form=contact_form)

