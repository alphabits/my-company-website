
BLOG_POSTS_PR_PAGE = 10

INSTALLED_MODULES = [
    ('blog', '/blog'),
    ('frontend', ''),
    ('quiz', '/quiz'),
    ('users', '/users')
]



try:
    from local_config import *
except ImportError, e:
    pass
