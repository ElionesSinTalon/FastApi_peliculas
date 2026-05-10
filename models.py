from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Pelicula(Base):
    __tablename__ = "peliculas"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)
    
    director = Column(String)
    duration = Column(Integer)
    format = Column(String)
    isPremiere = Column(Boolean)
    releaseDate = Column(String)
    posterUrl = Column(String)