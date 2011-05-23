from datetime import datetime
import os
import yaml

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Unicode
from sqlalchemy.orm import backref, relationship

from database import Base, DBModel
from utils import get_path

from modules.users.models import User


path = get_path(__file__)


class Question(Base, DBModel):
    __tablename__ = 'questions'

    id = Column(String, primary_key=True)
    title = Column(String)
    template = Column(String)
    status = Column(String, default='closed')
    opened_at = Column(Unicode(50), default=datetime.now)
    
    def is_closed(self):
        return self.status == 'closed'

    def open(self):
        self.opened_at = datetime.now()
        self.status = 'open'


class Answer(Base, DBModel):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    question_id = Column(String, ForeignKey('questions.id'))
    opened_at = Column(Unicode(50), default=datetime.now)
    closed_at = Column(Unicode(50))
    title = Column(String)
    body = Column(String)
    status = Column(String, default='open')
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship(User, backref=backref('answers', order_by=opened_at))
    question = relationship(Question, backref=backref('answers', order_by=opened_at))

    @classmethod
    def from_user_and_question(cls, user, question):
        return cls.query.filter(cls.user == user).filter(
                cls.question == question).all()


class Comment(Base):
    __tablename__ = 'answer_comments'

    id = Column(Integer, primary_key=True)
    answer_id = Column(Integer, ForeignKey('answers.id'))
    body = Column(String)
    created_at = Column(Unicode(50), default=datetime.now)


