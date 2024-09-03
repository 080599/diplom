from fastapi import APIRouter
from db.testservice import add_question_db, get_question, get_10_leaders,delete_exact_question

test_router=APIRouter(prefix='/question')

@test_router.post('/add_question_db')
async def add_question(main_question:str, v1:str, v2:str, v3:str, v4:str, correct_answer:str):
    return add_question_db(main_question=main_question,v1=v1, v2=v2, v3=v3, v4=v4, correct_answer=correct_answer)


@test_router.get('/get_questions')
async def get_questions_api():
    return get_question()

@test_router.get('/top-10-leaders')
async def get_10_leaders_api():
    return get_10_leaders()

@test_router.delete('delete_question')
async def delete_exact_question():
    return delete_exact_question()
