from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    question: str
    answer: str

@app.post("/rest/question", response_model=AnswerResponse)
async def get_answer(request: QuestionRequest):
    question = request.question.strip()
    answer = "Sorry, I don't know the answer to that question."
    return {"question": question, "answer": answer}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4080)
