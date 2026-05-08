from pydantic import BaseModel

class PeliculaBase(BaseModel):
    title: str
    overview: str
    year: int
    rating: float
    category: str
    
    director: str
    duration: int
    format: str
    isPremiere: bool
    releaseDate: str
    
class PeliculaCreate(PeliculaBase):
   pass 

class PeliculaResponse(PeliculaBase):
    id: int 
    
    class Config:
        from_attributes = True