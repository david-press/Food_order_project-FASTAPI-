# create DB configue

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./food.db" # questions concerning the link

engine = create_engine(DATABASE_URL) # to crete the database

sessionLocal = sessionmaker(bind = engine) #session = interaction layer with DB(a temporary workspace foe db operations)

Base = declarative_base()

# create models (Define Database Table)
from sqlalchemy import Column, String
