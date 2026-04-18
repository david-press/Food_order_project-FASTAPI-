from fastapi import FastAPI
from app.router.food_order import router as food_router
# crete the Table 
from database import engine, Base

Base.metadata.create_all(bind = engine)   




app = FastAPI()

app.include_router(food_router) #to include the router

