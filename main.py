from fastapi import FastAPI
from pydantic import BaseModel
from api.user_api import user_router
from api.test_api import test_router
from api.quizz_api import quiz_router
app = FastAPI(docs_url='/')
app.include_router(user_router)
app.include_router(test_router)
app.include_router(quiz_router)