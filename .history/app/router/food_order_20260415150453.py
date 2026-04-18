from datetime import datetime
import uuid
from app.storage.storage import load_data , save_data
from app.schema.schema import  get_info , order_food , bioOutput ,order_update , info_output 
from fastapi import APIRouter, HTTPException ,  status , Depends
from sqlalchemy.orm import Session
from app.database.deps import get_db


router = APIRouter(prefix="/api/v1/order" , tags=["food_order"])

@router.post("/" , response_model = bioOutput , status_code= status.HTTP_201_CREATED)
def create_bio(payload  : get_info):
    bio = load_data()
    new_bio = {
        "id" : str(uuid.uuid4()),
        "name" : payload.name,
        "age" : payload.age,
        "country" : payload.country,
        "status" : payload.status
    }
    bio.append(new_bio)
    save_data(bio)
    return new_bio

@router.post("/{user_id}" , response_model = info_output , status_code  = status.HTTP_201_CREATED)
def order_food(user_id : str , payload : order_food):
    """To order your food from a restaurant""" 
    order = load_data()
    for data in order:
        if data["id"] == user_id:
            new_bio = {
                "restaurant" : payload.restaurant,
                "food" : payload.food,
                "amount" : payload.amount,
                "status" : payload.status,
                }
            data.update(new_bio)
            save_data(order)
            return data
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail="ID Not found")   

@router.get("/{user_id}" , response_model= info_output )
def get_info(user_id  : str ):
    """Retrieve an entire data by an ID"""
    info = load_data()
    for data in info:
        if data["id"] == user_id:
            return data
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail="Data Not found")     


@router.put("/{user_id}", response_model= info_output , status_code= status.HTTP_202_ACCEPTED)
def update_order(user_id : str , payload : order_update):
    """To update the user Order"""
    orders = load_data()
    for index, order in enumerate(orders):
        if order["id"] == user_id:
            updated_order = order.copy()
            if payload.country is not None:
                updated_order["country"] = payload.country    
            if payload.restaurant is not None : 
                updated_order["restaurant"] = payload.restaurant
            if payload.food is not None:
                updated_order["food"] = payload.food
            if payload.amount is not None:
                updated_order["amount"] = payload.amount
            orders[index] = updated_order    
            save_data(orders)
            return updated_order
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail="ID Not found") 

@router.delete("/{user_id}" ,  status_code=status.HTTP_204_NO_CONTENT)  
def delete_order(user_id : str):
    """Delete an unwanted order""" 
    orders = load_data()
    for index , data in enumerate(orders):
       if data["id"] == user_id:
           orders.pop(index)
           save_data(orders)
           return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail="Issue Not found")    







