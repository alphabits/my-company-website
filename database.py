from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import config


Base = declarative_base()

engine = create_engine(config.DB_CONNECTION, convert_unicode=True)
if config.DEBUG:
    engine.echo = True

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, 
        bind=engine))


class DBModel(object):

    def save(self):
        db_session.add(self)
        db_session.commit()


Base.query = db_session.query_property()

def init_db():
    application.load_models(config.INSTALLED_MODULES)
    Base.metadata.create_all(bind=engine)


import app as application

@application.app.after_request
def shutdown_session(response):
    db_session.remove()
    return response
