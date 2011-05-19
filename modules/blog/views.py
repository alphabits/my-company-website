import os
from flask import Module, url_for, render_template, request

from .models import get_posts, num_posts
import config


blog = Module(__name__, 'blog')


@blog.route('/')
def index():
    page_size = config.BLOG_POSTS_PR_PAGE
    total_posts = num_posts()
    page = int(request.args.get('page', 1))
    if page < 1:
        page = 1
    posts = get_posts((page-1)*page_size, page*page_size)
    return render_template('blog/index.html', **locals())
