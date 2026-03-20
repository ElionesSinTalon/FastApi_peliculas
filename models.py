from sqlalchemy import Column, Integer, String, Float
from database import Base

class Pelicula(Base):
    __tablename__ = "peliculas"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)