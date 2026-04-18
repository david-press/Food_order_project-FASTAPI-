#create models (Define Database Table)

from sqlalchemy import Column, String , Integer
from database import Base

class User(Base):
    __tablename__ = "users" #the name of the table created
    id = Column(String , primary)



