#create models (Define Database Table)

from sqlalchemy import Column, String , Integer
from database import Base

class User(Base):
    __tablename__ = "users" #the name of the table created
    id = Column(String , primary_key= True , index = True)
    name = Column(String)
    age = Column(Integer)
    country = Column(String)
    restaurant = Column(String)
    food = Column(String)
    amount = Column(Integer)

# crete the Table 

Base.metadata   



