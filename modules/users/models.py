from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)


def authorize(username, password):
    res = User.query.filter(User.username == username).all()
    if len(res) == 1 and res[0].password == password:
        return res[0]
    return False

def generate_password(password):
    return "lol" + password
