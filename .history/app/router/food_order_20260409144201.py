import uuid
from app.storage.storage import load_data , save_data
from app.schema.schema import  get_info , order_food ,  info_output 
from fastapi import APIRouter, HTTPException ,  status

router = APIRouter(prefix="/api/v1/order" , tags=["food_order"])

@router.get("/" , response_model= list[get_info ])

