from pydantic import BaseModel

class PeliculaBase(BaseModel):
    title: str
    overview: str
    year: int
    rating: float
    category: str
    
class PeliculaCreate(PeliculaBase):
   pass 

class PeliculaResponse(PeliculaBase):
    id: int 
    
    class Config:
        from_attributes = True