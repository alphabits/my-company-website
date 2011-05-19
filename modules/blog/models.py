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
        fobj = open(path+'/'+f, 'r')
        tmp_post = yaml.load(fobj)
        tmp_post['filename'] = f
        fobj.close()
        posts.append(tmp_post)
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
        with open(path+'/'+idx[k], 'r') as f:
            tmp_post = yaml.load(f)
        tmp_post['filename'] = idx[k]
        posts.append(tmp_post)
    return posts

def num_posts():
    return len([f for f in os.listdir(path) if not f[0] in ['.', '_']])

