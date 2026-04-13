from pydantic import BaseModel
from fastapi import FastAPI , APIRouter
from app.router.food_order import router as food_router

app = FastAPI

pp.include_router(issues_router) #to include the router

