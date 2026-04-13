from pydantic import BaseModel , Field
from typing import Optional
from enum import Enum

class Status(Enum):
    pending = "Processing"
    completed = "Saved"

class get_info(BaseModel):
    name : str = Field(..., min_length= 3 , max_length=100)
    age : int
    country : str
    status : Status = Status.pending

class order_food(BaseModel):
    restaurant : str
    food : str
    amount : int
    status : Status = Status.pending

class info_output(BaseModel):
    id : str
    name : str
    country : str
    restaurant : str
    food : str
    total_amount : int
    status : Status = Status.completed






