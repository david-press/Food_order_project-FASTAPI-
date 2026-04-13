import uuid
from app.storage.storage import load_data , save_data
from app.schema.schema import  get_info , order_food , order_update , info_output 
from fastapi import APIRouter, HTTPException ,  status

router = APIRouter(prefix="/api/v1/order" , tags=["food_order"])

@router.post("/" , response_model = get_info , status_code= status.HTTP_201_CREATED)
def create_bio(payload  : get_info):
    bio = load_data()
    new_bio = {
        "id" : str(uuid.uuid4),
        "name" : payload.name,
        "age" : payload.age,
        "country" : payload.country,
        "date_created" : payload.created_at,
        "status" : payload.status
    }
    bio.append(new_bio)
    save_data(bio)
    return new_bio

@router.post("/{user_id}" , response_model = info_output , status_code= status.HTTP_202_ACCEPTED)
def order_food(user_id : str , payload = order_food):
    """To order your food from a restaurant""" 
    order = load_data()
    for data in order:
        if order["id"] == user_id:
            new_bio = {
                "restaurant" : payload.restaurant,
                "food" : payload.food,
                "amount" : payload.amount,
                "status" : payload.status,
                "date_ordered" : payload.created_at,
                }
            order.append(new_bio)
            save_data(order)
            return order
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail="ID Not found")    

@router.put("/{user_id}", response_model= info_output , status_code= status.HTTP_102_PROCESSING)
def update_order(user_id : str , payload = order_update):
    """To update the user Order"""
    orders = load_data()
    for index, order in enumerate(orders):
        if orders["id"] == user_id:
             





