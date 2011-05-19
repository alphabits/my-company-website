from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

import config
import app as application

engine = create_engine(config.DB_CONNECTION, convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, 
        bind=engine))

Base.query = db_session.query_property()

def init_db():
    application.load_models(config.INSTALLED_MODULES)
    Base.metadata.create_all(bind=engine)

@application.app.after_request
def shutdown_session(response):
    db_session.remove()
    return response
