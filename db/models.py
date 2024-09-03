from db import Base
from sqlalchemy import Column, Integer,String,DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from datetime import datetime

class User(Base):
    __tablename__='users'
    id= Column(Integer, autoincrement=True, primary_key=True)
    name= Column(String, nullable=False)
    phone_number= Column(String,nullable=False)
    level= Column(String,default='Select your level', nullable=False)
    datetime=Column(DateTime)
class Question(Base):
    __tablename__='question'
    id= Column(Integer, autoincrement=True, primary_key=True)
    main_question= Column(String, nullable=False)
    v1=Column(String)
    v2=Column(String)
    v3=Column(String)
    v4=Column(String)
    correct_answer= Column(String,nullable=False)
    timer=Column(DateTime)
class Result(Base):
    __tablename__="results"
    id=Column(Integer,autoincrement=True,primary_key=True)
    user_id=Column(Integer, ForeignKey('users.id'))
    correct_answer=Column(Integer,default=0)
    level=Column(String, nullable=False)
    user_fk=relationship(User, foreign_keys=[user_id], lazy='subquery')

class UserAnswer(Base):
    __tablename__='user_answer'

    id=Column(Integer, autoincrement=True,primary_key=True)
    user_id=Column(Integer, ForeignKey('user.id'))
    question_id=Column(Integer,ForeignKey('question.id'))
    level=Column(String, ForeignKey('users.level'))
    user_answer=Column(String)
    correctness=Column(Boolean,default=False)
    timer=Column(DateTime)

    user_fk=relationship(User,ForeignKey[user_id], lazy='subquery')
    question_fk=relationship (Question, ForeignKey[question_id],lazy='subquery')

class Quiz(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    questions = relationship("Question", back_populates="topic")

