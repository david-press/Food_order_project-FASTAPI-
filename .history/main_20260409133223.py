from pydantic import BaseModel
from fastapi import FastAPI , APIRouter

app = FastAPI

class Task(BaseModel):
    title : str
    complete : bool = False

task = Task(title = "David")
@app.get("/Testing")
def get_info():
