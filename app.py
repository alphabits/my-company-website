from flask import Flask

import config


# Order of the following instructions matters.
# You'll get an error if the app object is not 
# created before importing the views.
# The reason is that the views depend on the 
# utils module and the utils module depends on
# the app object

app = Flask(__name__)

from apps.blog.views import blog
from apps.frontend.views import frontend

app.register_module(blog, url_prefix='/blog')
app.register_module(frontend)
app.config.from_object(config)
