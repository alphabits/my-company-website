from flask import Flask
import alphabits.config as config
from apps.blog.views import blog
from apps.frontend.views import frontend

app = Flask(__name__)
app.register_module(blog, url_prefix='/blog')
app.register_module(frontend)
app.config.from_object(config)

import utils
