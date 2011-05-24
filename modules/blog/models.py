from __future__ import with_statement

import os

import yaml

from utils import get_path


path = get_path(__file__) + '/posts'

def get_all_posts():
    posts = []
    for f in os.listdir(path):
        if f.startswith('.') or f.startswith('_'):
            continue
        posts.append(get_post_from_yaml(f))
    posts.sort(key=lambda p: p['date'], reverse=True)
    return posts

def get_posts(start, end):
    posts = []
    with open(path+'/_index_file.yaml', 'r') as f:
        idx = yaml.load(f)
    keys = idx.keys()
    keys.sort(reverse=True)
    keys = keys[start:end]
    for k in keys:
        posts.append(get_post_from_yaml(idx[k]))
    return posts

def get_post_from_yaml(filename):
    with open(path+'/'+filename, 'r') as f:
        post = yaml.load(f)
    post['filename'] = filename
    return post

def num_posts():
    return len([f for f in os.listdir(path) if not f[0] in ['.', '_']])

