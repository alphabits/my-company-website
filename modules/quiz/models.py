from sqlalchemy import Column, Integer, String

from database import Base



class Question(object):

    def __init__(self, question_id):
        self.question_id = question_id

def get_questions():
    pass

