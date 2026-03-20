from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session 
import models, dtos
import peliculas.crud as crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
 
def get_db(): 
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()
 
@app.get("/peliculas/{pelicula_id}", response_model=dtos.PeliculaResponse)
def get_pelicula(pelicula_id: int, db:Session = Depends(get_db)):
    db_pelicula = crud.find_pelicula(db = db, pelicula_id = pelicula_id)
    
    if db_pelicula is None:
        raise HTTPException(status_code = 404, detail = "Pelicula no existente")
    return db_pelicula 

@app.get("/peliculas", response_model=list[dtos.PeliculaResponse])
def get_peliculas(db:Session = Depends(get_db)):
   peliculas = crud.get_peliculas(db = db)
   return peliculas

@app.post("/peliculas", response_model=dtos.PeliculaResponse)
def crear_pelicula(pelicula: dtos.PeliculaCreate, db: Session = Depends(get_db)):
    return crud.create_pelicula(db = db, pelicula = pelicula)

@app.put("/peliculas/{pelicula_id}", response_model=dtos.PeliculaResponse)
def actualizar_pelicula(pelicula_id: int, pelicula: dtos.PeliculaCreate, db: Session = Depends(get_db)):
    pelicula_db = crud.actualizar_pelicula(db = db, pelicula_id = pelicula_id, pelicula_update = pelicula) 
    
    if pelicula_db is None:
        raise HTTPException(status_code = 404, detail = "Pelicula no existente")
    return pelicula_db

@app.delete("/peliculas/{pelicula_id}", response_model = dtos.PeliculaResponse)
def eliminar_pelicula(pelicula_id: int, db: Session = Depends(get_db)):
    pelicula_db = crud.eliminar_pelicula(db = db, pelicula_id = pelicula_id) 
    
    if pelicula_db is None:
        raise HTTPException(status_code = 404, detail = "Pelicula no existente")
    return pelicula_db
  