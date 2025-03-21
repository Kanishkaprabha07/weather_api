from sqlalchemy import Column, Integer, String
from db import Base 

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    abbreviation = Column(String)
