from pydantic import BaseModel
from fastapi import FastAPI , APIRouter
from app.router.food_order import router as f

app = FastAPI

