#create models (Define Database Table)

from sqlalchemy import Column, String , Integer
from app.database.database import Base,  engine

class User(Base):
    __tablename__ = "users" #the name of the table created
    id = Column(String , primary_key= True , index = True)
    name = Column(String)
    age = Column(Integer)
    country = Column(String)
    
    
    status = Column(String)
    amount = Column(Integer)

class Order(Base):
    __tablename__ = "orders"
    id = Column(String , primary_key= True , index = True)
    restaurant = Column(String)
    food = Column(String)

