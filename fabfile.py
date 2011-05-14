from __future__ import with_statement

from fabric.api import *


env.hosts = ['anders@173.45.237.53:30010']


def deploy():
    code_dir = '/home/anders/alphabits.dk/application'
    local('git add .')
    local('git commit -m "Deployment commit"')
    local('git push origin master')
    with cd(code_dir):
        run('git pull origin')
        run('touch app.wsgi')
