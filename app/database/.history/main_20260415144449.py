# crete the Table 
from database import engine, Base
Base.metadata
Base.metadata.create_all(bind = engine)   



