from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.deps import get_db
## contrato da API - schemas
from app.schemas.cargo import CargoCreate, CargoOut, CargoUpdate
from app.repositories import cargo as repo
from app.services.cargo import criar_cargo

rotas = APIRouter(prefix="/v1/Cargo", tags=["Cargo"])

@rotas.post("/", response_model=CargoOut, status_code=status.HTTP_201_CREATED)
def create(payload: CargoCreate, db: Session = Depends(get_db)):
    #preco = payload.preco
    #if preco <= 0:
    #    raise HTTPException(status.HTTP_400_BAD_REQUEST, "Preco deve ser maior que zero")
    criar_cargo(payload)
    return repo.create(db, payload)

@rotas.get("/", response_model=list[CargoOut])
def list_all(db: Session = Depends(get_db)):
    return repo.get_all(db)

@rotas.get("/{cargo_id}", response_model=CargoOut)
def get_id(cargo_id: int, db: Session = Depends(get_db)):
    objeto = repo.get(db, cargo_id)
    if not objeto: 
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Cargo não encontrado")
    return objeto

@rotas.put("/{cargo_id}", response_model=CargoOut)
def update(cargo_id: int, payload: CargoUpdate, db: Session = Depends(get_db)):
    objeto = repo.get(db, cargo_id)
    if not objeto:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Cargo não encontrado")
    
    return repo.update(db, cargo_id, payload)

@rotas.delete("/{cargo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(cargo_id: int, db: Session = Depends(get_db)):
    objeto = repo.get(db, cargo_id)
    if not objeto:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Cargo não encontrado")
    
    repo.delete(db, cargo_id)
    return None