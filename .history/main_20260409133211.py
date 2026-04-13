from pydantic import BaseModel
from fastapi import FastAPI , APIRouter

app = FastAPI

class Task(BaseModel):
    title : str
    complete : bool = False

task = 
@app.get("/Testing")
def get_info():
