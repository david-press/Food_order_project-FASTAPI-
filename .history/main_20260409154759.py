from pydantic import BaseModel
from fastapi import FastAPI , APIRouter
from app.router.food_order import router as food_router

app = FastAPI

app.include_router(foof) #to include the router

