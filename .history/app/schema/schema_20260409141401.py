from pydantic import BaseModel , Field
from typing import Optional
from enum import Enum

class Status(Enum):
    pending = "Processing"
    completed = "Saved"

class get_info(BaseModel):
    name : str = Field(..., min_length= 3 , max_length=30)
    age : int = Field(..., min_length= 1 , max_length=3)
    country : str = Field(..., min_length= 5 , max_length=20)
    status : Status = Status.pending

class order_food(BaseModel):
    restaurant : str = Field(..., min_length= 3 , max_length=30)
    food : str = Field(..., min_length= 1 , max_length=3)
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






