from flask import Flask

import config


# Order of the following instructions matters.
# You'll get an error if the app object is not 
# created before importing the views.
# The reason is that the views depend on the 
# utils module and the utils module depends on
# the app object

app = Flask(__name__)
app.config.from_object(config)

app.secret_key = config.SECRET_KEY

def load_modules(modules):
    for mod_name, url_root in modules:
        tmp_mod_views = __import__('modules.%s.views' % mod_name, globals(), 
                locals(), [mod_name], -1)
        app.register_module(tmp_mod_views.__dict__[mod_name], 
                url_prefix=url_root)

def load_models(modules):
    for mod_name, url_root in modules:
        tmp_mod_model = __import__('modules.%s.models' % mod_name, globals(),
                locals(), [mod_name], -1)


load_modules(config.INSTALLED_MODULES)

'''
from modules.blog.views import blog
app.register_module(blog, url_prefix='/blog')

from modules.frontend.views import frontend
app.register_module(frontend, url_prefix='')
'''
