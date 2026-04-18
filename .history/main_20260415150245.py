from fastapi import FastAPI
from app.router.food_order import router as food_router
from app.database.database import engine, Base # crete the Table 

app = FastAPI()

app.include_router(food_router) #to include the router
Base.metadata.create_all(bind = engine)   