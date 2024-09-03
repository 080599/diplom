from typing import List, Optional

from fastapi import FastAPI, HTTPException, Path, Body
from pydantic import BaseModel, Field

from db.models import Quiz

app = FastAPI()

quizzes = {
    1: Quiz(id=1, topic="Films", questions=["?"]),
    2: Quiz(id=2, topic="География", questions=["?"]),
}

@app.get("/quizzes", response_model=List[Quiz])
async def get_quizzes(quizzes=None):
    return list(quizzes.values())

@app.get("/quizzes/{quiz_id}", response_model=Quiz)
async def get_quiz(quiz_id: int = Path(..., gt=0)):
    quiz = quizzes.get(quiz_id)
    if quiz is None:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz

@app.post("/quizzes", response_model=Quiz)
async def create_quiz(quiz: Quiz = Body(...), quizzes=None):
    next_id = max(quizzes.keys()) + 1
    quiz.id = next_id
    quizzes[next_id] = quiz
    return quiz

@app.put("/quizzes/{quiz_id}", response_model=Quiz)
async def update_quiz(quiz_id: int = Path(..., gt=0), quiz: Quiz = Body(...), quizzes=None):
    if quiz_id not in quizzes:
        raise HTTPException(status_code=404, detail="Quiz not found")
    quizzes[quiz_id] = quiz
    return quiz

@app.delete("/quizzes/{quiz_id}")
async def delete_quiz(quiz_id: int = Path(..., gt=0)):
    if quiz_id not in quizzes:
        raise HTTPException(status_code=404, detail="Quiz not found")
    del quizzes[quiz_id]
    return {"message": "Quiz deleted"}

@app.patch("/quizzes/{quiz_id}/topic", response_model=Quiz)
async def update_quiz_topic(quiz_id: int = Path(..., gt=0), topic: str = Body(...), quizzes=None):
    if quiz_id not in quizzes:
        raise HTTPException(status_code=404, detail="Quiz not found")
    quizzes[quiz_id].topic = topic
    return quizzes[quiz_id]