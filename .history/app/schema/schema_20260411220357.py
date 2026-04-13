from datetime import datetime
from pydantic import BaseModel , Field , field_validator
from fastapi import HTTPException
from typing import Optional
from enum import Enum

class Status(str , Enum):
    pending = "Processing"
    completed = "Done"

class get_info(BaseModel):
    name : str = Field(..., min_length= 3 , max_length=30)
    age : int = Field(..., ge= 1 , le=120) #int constraints ge , le , lt, gt

    @field_validator("age" , mode = "after")
    def validate_age(cls , value):
        if not isinstance(value , int):
            raise ValueError("Age must be integer , not string")
        if value < 0 :
            raise ValueError("Age cannot be negative")
        if value > 130 :
            raise ValueError("Age is unrealistic")
        return value

    country : str = Field(..., min_length= 5 , max_length=20)
    status : Status = Status.pending

class bioOutput(BaseModel):
    id: str
    name: str
    age: int
    country: str
    status: Status : Status = Status.comp

class order_food(BaseModel):
    restaurant : str = Field(..., min_length= 3 , max_length=30)
    food : str = Field(..., min_length= 4 , max_length= 500)
    amount : int = Field(..., ge= 5 , le=30000)

    @field_validator("amount" , mode= "before") 
    def validate_amount(cls , value):
        if value > 20000 : 
            raise ValueError("You can only make a purchase of over thousand online")
        if not isinstance(value , int):
            raise ValueError("Enter Amounts in digits")
        return value
    status : Status = Status.pending

class order_update(BaseModel):
    country : Optional[str] = Field(default=None, max_length=12)
    restaurant : Optional[str] = Field(default=None, max_length=30)
    food : Optional[str] = Field(default=None, max_length=500)
    amount : Optional[int] = Field(default=None, ge=5, le=30000)
    status : Status = Status.pending




class info_output(BaseModel):
    id : str
    name : str
    country : str
    restaurant : str
    food : str
    amount : int
    status : Status = Status.completed




