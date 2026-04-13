from datetime import datetime
from pydantic import BaseModel , Field , field_validator
from fastapi import HTTPException
from typing import Optional
from enum import Enum

class Status(str , Enum):
    pending = "Processing"
    completed = "Saved"

class get_info(BaseModel):
    name : str = Field(..., min_length= 3 , max_length=30)
    age : int = Field(..., min_length= 1 , max_length=3)

    @field_validator("age" , mode = "before")
    def validate_age(cls , value):
        if any(char.isalpha() for char in value):
            raise ValueError("Age mst be in digits")
        return value.strip().amount()

    country : str = Field(..., min_length= 7 , max_length=12)
    created_at : datetime
    status : Status = Status.pending

class order_food(BaseModel):
    restaurant : str = Field(..., min_length= 3 , max_length=30)
    food : str = Field(..., min_length= 4 , max_length= 500)
    amount : int = Field(..., min_length= 1 , max_length=5)

    @field_validator("amount", mode= "before")
    def validate_amount(cls , value):
        if len(value) > 5 :
            raise ValueError("You can only make a purchase of over thousand online")
        if any(char.isalpha() for char in value):
            raise ValueError("Enter Amounts in digits")
        return value.strip().amount()
    created_at : datetime

    status : Status = Status.pending

class order_update(BaseModel):
    country : Optional[str] = Field(default=None, max_length=12)
    restaurant : Optional[str] = Field(default=None, max_length=30)
    



class info_output(BaseModel):
    id : str
    name : str
    country : str
    restaurant : str
    food : str
    total_amount : int
    created_at : datetime
    status : Status = Status.completed




