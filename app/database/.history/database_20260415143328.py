# create DB configue

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./food.db" # questions concerning the link

engine = create_engine(DATABASE_URL) # to crete the database

sessionLocal = sessionmaker(bind = engine) #session = interaction 

Base = declarative_base()
