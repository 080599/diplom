from db import get_db
from db.models import Question, Result

def add_question_db(main_question,v1, v2,v3, v4,correct_answer):
    with next(get_db()) as db:
        new_question= Question(main_question=main_question, v1=v1, v2=v2, v3=v3,v4=v4, correct_answer=correct_answer)
        db.ad(new_question)
        db.commit()
        return 'Question successfully added'

def get_question():
    with next(get_db()) as db:
        question= db.query(Question).all()
        return question[:20]


def get_10_leaders():
    with next(get_db()) as db:
        leaders=db.query(Result.user_id).order_by(Result.correct_answer.desc())
        return leaders[:10]


def delete_exact_question(main_question):
    with next(get_db()) as db:
        delete_question = Question(main_question=main_question)
        db.delete(delete_question)
        db.commit()
        return 'Question successfully deleted'