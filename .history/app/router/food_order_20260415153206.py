from datetime import datetime
import uuid
from app.schema.schema import  get_info , order_food , bioOutput ,order_update , info_output 
from fastapi import APIRouter, HTTPException ,  status , Depends
from sqlalchemy.orm import Session
from app.database.deps import get_db
from app.database.models import User

router = APIRouter(prefix="/api/v1/order" , tags=["food_order"])

@router.post("/" , response_model = bioOutput , status_code= status.HTTP_201_CREATED)
def create_bio(payload  : get_info , db : Session = Depends(get_db)):
    new_bio = User(
        id = str(uuid.uuid4()),
        name = payload.name,
        age = payload.age,
        country = payload.country,
        status = payload.status
    )
    db.add(new_bio) #to add or append to the db
    db.commit()
    return new_bio

@router.post("/{user_id}" , response_model = info_output , status_code  = status.HTTP_201_CREATED)
def order_food(user_id : str , payload : order_food , db : Session = Depends(get_db)):
    """To order your food from a restaurant""" 
    order = db.query(User).filter(User.id == user_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail="ID Not found")  
    
    new_order = User(
        restaurant = payload.restaurant,
        food = payload.food,
        amount = payload.amount,
        status = payload.status,
    )
    db.add(new_order) #to add or append to the db
    db.commit()
            
    return new_order
     

@router.get("/{user_id}" , response_model= info_output )
def get_info(user_id  : str, db : Session = Depends(get_db)):
    """Retrieve an entire data by an ID"""
    info = db.query(User).filter(User.id == user_id).first()
    if not info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail="ID Not found")
    return info  
    


@router.put("/{user_id}", response_model= info_output , status_code= status.HTTP_202_ACCEPTED)
def update_order(user_id : str , payload : order_update , db : Session = Depends(get_db)):
    """To update the user Order"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail="ID Not found")
    
    user.country = payload.country
    user.restaurant = payload.restaurant
    user.food = payload.food
    user.amount = payload.amount
    user.status = payload.status 

    db.commit()
    db.refresh(user)
    return user  

@router.delete("/{user_id}" ,  status_code=status.HTTP_204_NO_CONTENT)  
def delete_order(user_id : str , db : Session = Depends(get_db)):
    """Delete an unwanted order""" 
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail="ID Not found")
    
    db.delete()
    db.commit()

    return {"m"}







