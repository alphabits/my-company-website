import os
import yaml
import markdown
from flask import Module, url_for, render_template


blog = Module(__name__, 'blog')

path = os.path.abspath(os.path.dirname(__file__)) + '/posts'

md = markdown.Markdown(extensions=['codehilite'])

@blog.route('/')
def index():
    posts = []
    for f in os.listdir(path):
        if f.startswith('.'):
            continue
        fobj = open(path+'/'+f, 'r')
        tmp_post = yaml.load(fobj)
        fobj.close()
        tmp_post['body'] = md.convert(tmp_post['body'])
        posts.append(tmp_post)
    return render_template('blog/index.html', posts=posts)
