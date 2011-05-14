ENV = 'prod'

SOME_SETTING = "setting value"
BLOG_POSTS_PR_PAGE = 10


if ENV == 'dev':
    DB = 'dev.db'
    
elif ENV == 'prod':
    DB = 'prod.db'
