from sqlalchemy.orm import Session 
from models import Pelicula 
import dtos 

def get_peliculas(db: Session):
    return db.query(Pelicula).all()

def find_pelicula(db: Session, pelicula_id: int):
    return db.query(Pelicula).filter(Pelicula.id == pelicula_id).first()

def create_pelicula(db: Session, pelicula: dtos.PeliculaCreate):
    db_pelicula = Pelicula(
        title = pelicula.title,
        overview = pelicula.overview,
        year = pelicula.year,
        rating = pelicula.rating,
        category = pelicula.category
    )  
    
    db.add(db_pelicula) 
    db.commit()
    db.refresh(db_pelicula)
    return db_pelicula
    
def actualizar_pelicula(db: Session, pelicula_id: int, pelicula_update: dtos.PeliculaCreate):
    db_pelicula = find_pelicula(db, pelicula_id)
    
    if db_pelicula:
       db_pelicula.title = pelicula_update.title
       db_pelicula.overview = pelicula_update.overview
       db_pelicula.year = pelicula_update.year
       db_pelicula.rating = pelicula_update.rating
       db_pelicula.category = pelicula_update.category
       
       db.commit()
       db.refresh(db_pelicula)
       return db_pelicula 
    
def eliminar_pelicula(db: Session, pelicula_id: int):
    db_pelicula = find_pelicula(db, pelicula_id)
    
    if db_pelicula:
        db.delete(db_pelicula)
        db.commit()
        return db_pelicula
    
    