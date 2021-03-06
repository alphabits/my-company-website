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
    languages_allowed = Column(String)

    def open_for_user(self, user):
        if len(Answer.from_user_and_question(user, self)) == 0:
            a = Answer(type='opener', user=user, question=self)
            a.save()
            self.answers.append(a)
    
    def opened_by_user(self, user):
        return len(Answer.from_user_and_question(user, self)) > 0

    def get_languages_allowed(self):
        return self.languages_allowed.split(',')


class Answer(Base, DBModel):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    question_id = Column(String, ForeignKey('questions.id'))
    opened_at = Column(Unicode(50), default=datetime.now)
    updated_at = Column(Unicode(50))
    title = Column(String)
    body = Column(String)
    type = Column(String) # opener, text
    language = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship(User, backref=backref('answers', order_by=opened_at))
    question = relationship(Question, backref=backref('answers', order_by=opened_at))

    @classmethod
    def from_user_and_question(cls, user, question):
        return cls.query.filter(cls.user == user).filter(
                cls.question == question).all()

