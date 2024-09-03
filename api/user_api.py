from pathlib import Path

from fastapi import APIRouter, Request, Depends, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from db import get_db
from db.models import Quiz
from db.userservice import register_user_db, get_all_users, get_result_user_db, user_answer_db
from db.topicservice import Session, get_all_topics

user_router= APIRouter(prefix='/user')
@user_router.get('/register_user')
async def register_user(name=str, phone_number=str,level=str):
    user=register_user_db(name=name, phone_number=phone_number, level=level)
    return {'status':1, "message":user}
@user_router.get('/get_all_users')
async def get_all_users_api():
    return get_all_users()
@user_router.post('/answer_done')
async def get_answer(user_id:int, q_id:int, level:str, user_answer:str):
    user=user_answer_db(q_id=q_id, user_id=user_id, level=level, user_answer=user_answer)
    return f'answer {user}'

@user_router.get('/result')
async def user_result(user_id):
    return get_result_user_db(user_id)

@user_router.delete('delete_user')
async def delete_user(user_id):
    return delete_user(user_id)









