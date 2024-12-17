from pprint import pprint
from fastapi import FastAPI
from pydantic import BaseModel

from dotenv import load_dotenv
from workflow import workflow

load_dotenv()

# Compile
compiled_workflow = workflow.compile()

fastapi_app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    question: str
    answer: str

@fastapi_app.post("/rest/question", response_model=AnswerResponse)
async def get_answer(request: QuestionRequest):
    question = request.question.strip()
    inputs = {
        "question": question
    }

    for output in compiled_workflow.stream(inputs):
        for key, value in output.items():
            # Node
            pprint(f"Node '{key}':")
            # Optional: print full state at each node
            # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
        pprint("\n---\n")
    
    answer = value["generation"]#"Sorry, I don't know the answer to that question."
    return {"question": question, "answer": answer}
