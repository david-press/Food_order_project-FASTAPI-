from pydantic import BaseModel , Field
from typing import Optional
from enum import Enum

class Status(Enum):
    pending = "Processing"
    completed = "Saved"

class get_info(BaseModel):
    name : str
    age : int
    country : str
    status : Status = Status.pending

class order_food(BaseModel):
    restaurant : str
    food : str
    amount : int
    status : Status = Status.pending

class info_output




