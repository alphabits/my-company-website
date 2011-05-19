import os
import yaml

from sqlalchemy import Column, Integer, String

from database import Base
from utils import get_path

path = get_path(__file__)


class Question(object):

    def __init__(self, question_id):
        self.question_id = question_id


class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    question_id = Column(String)


_questions = []

def load_questions():
    if not _questions:
        for filename in os.listdir('%s/questions' % path):
            if not filename.startswith('.'):
                q = yaml.load(open('%s/questions/%s' % (path, filename)))
                _questions.append(q)


def get_questions():
    load_questions()
    return _questions


def get_question_by_id(id):
    load_questions()
    for q in _questions:
        if q["id"] == id:
            return q
    return None


