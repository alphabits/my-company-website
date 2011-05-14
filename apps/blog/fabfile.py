from __future__ import with_statement

import os

from fabric.api import *
import yaml


env.hosts = ['anders@173.45.237.53:30010']

def test():
    index_data = {}
    for filename in os.listdir('posts'):
        if filename[0] in ['.', '_']:
            continue;
        post = yaml.load(open('posts/'+filename))
        index_data[post['date']] = filename
        output = yaml.dump(index_data, open('posts/_index_file.yaml', 'w'), indent=4,
                default_flow_style=False)

def deploy():
    code_dir = '/home/anders/alphabits.dk/application'
    local('git add .')
    local('git commit -m "Deployment commit"')
    local('git push origin master')
    with cd(code_dir):
        local('git pull origin master')
        local('touch app.wsgi')

def ext_test():
    run('ls')
