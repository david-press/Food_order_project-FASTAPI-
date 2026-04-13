from fastapi import FastAPI
from app.router.food_order import router as food_router

app = FastAPI()

app.include_router(food_router) #to include the router

