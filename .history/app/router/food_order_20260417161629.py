import asyncio 
import uuid
from app.schema.schema import  get_info , order_food , bio_output ,order_update , info_output , order_output 
from fastapi import APIRouter, HTTPException ,  status , Depends
from sqlalchemy.orm import Session
from app.database.deps import get_db
from app.database.models import User , Order

router = APIRouter(prefix="/api/v1/order" , tags=["food_order"])
details = "ID not found"

# @router.get("/{user_id}" , response_model= order_output )
# async def get_info(user_id  : str, order_id : str , db : Session = Depends(get_db)):
#     """Retrieve an entire data by an ID"""
#     order = db.query(Order).filter(Order.order_id == order_id , Order.user_id == user_id ).first()
#     if not order:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=details)
#     return order
@router.get("/{user_id}")
async def get_info(user_id  : str, db : Session = Depends(get_db)):
    """Retrieve an entire data by an ID"""
    user_task = asyncio.to_thread(get_user , db , user_id)
    orders_task = asyncio.to_thread(get_orders , db , user_id)

    users , orders = await asyncio.gather(user_task , orders_task)

    return {}

    order = db.query(Order).filter(Order.order_id == order_id , Order.user_id == user_id ).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=details)
    return order

@router.post("/" , response_model = bio_output , status_code= status.HTTP_201_CREATED)
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
    db.refresh(new_bio)
    return new_bio

@router.post("/{user_id}" , response_model = order_output , status_code  = status.HTTP_201_CREATED)
def order_food(user_id : str , payload : order_food , db : Session = Depends(get_db)):
    """To order your food from a restaurant"""

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail= details)
    
    new_order = Order(
        order_id = str(uuid.uuid4()),
        user_id = user_id, #this links the 2 tables from both post together
        restaurant = payload.restaurant,
        food = payload.food,
        amount = payload.amount,
        status = payload.status,
    )
    db.add(new_order) #to add or append to the db
    db.commit()
    db.refresh(new_order)
            
    return new_order
    


@router.put("/{order_id}", response_model= order_output , status_code= status.HTTP_202_ACCEPTED)
def update_order(order_id : str , payload : order_update , db : Session = Depends(get_db)):
    """To update the user Order"""
    order = db.query(Order).filter(Order.order_id == order_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=details)
    
    order.restaurant = payload.restaurant
    order.food = payload.food
    order.amount = payload.amount
    order.status = payload.status 

    db.commit()
    db.refresh(order)
    return order  

@router.delete("/{user_id}/orders/{order_id}"  ,  status_code=status.HTTP_204_NO_CONTENT)  
def delete_order(order_id : str , user_id : str , db : Session = Depends(get_db)):
    """Delete an unwanted order""" 
    order = db.query(Order).filter(Order.order_id == order_id , Order.user_id == user_id ).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=details)
    
    db.delete(order)
    db.commit()

    return {"message" : "DELETED"}







