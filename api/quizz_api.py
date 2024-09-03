from db.topicservice import create_topic, get_all_topics,delete_topic
from fastapi import APIRouter


quiz_router=APIRouter(prefix='/quizz')


@quiz_router.post('/create_topic')
async def create_topic():
    return create_topic

@quiz_router.get('get_all_topics')
async def get_topics():
    return get_topics()


@quiz_router.delete('delete_topic')
async def delete_topic():
    return delete_topic()

