import uuid
from app.storage.storage import load_data , save_data
from app.schema.schema import  get_info , order_food ,  info_output 
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
    save_data(new_bio)

