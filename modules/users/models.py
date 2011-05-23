from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String, default='member')

    def __init__(self, username=None, email=None, password=None, role=None):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return '<User %r>' % (self.username)

anonymous = User(username='Anonymous', password='', email='', role='anonymous')


def authorize(username, password):
    res = User.query.filter(User.username == username).filter(
            User.password == password).all()
    return len(res) == 1 and res[0].role in ['member', 'admin']

def generate_password(password):
    return "lol" + password
