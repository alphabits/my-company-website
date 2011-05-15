from __future__ import with_statement

import os

from fabric.api import *
import yaml


def test():
    index_data = {}
    for filename in os.listdir('posts'):
        if filename[0] in ['.', '_']:
            continue;
        post = yaml.load(open('posts/'+filename))
        index_data[post['date']] = filename
        output = yaml.dump(index_data, open('posts/_index_file.yaml', 'w'), indent=4,
                default_flow_style=False)

def ext_test(test):
    print test
