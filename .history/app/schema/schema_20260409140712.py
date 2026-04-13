from pydantic import BaseModel , Field
from typing import Optional
from enum import Enum

class Status(Enum):
    pending = "Processing"
    completed = "Saved"

class get_info(BaseModel):
    

class order_food(BaseModel):





