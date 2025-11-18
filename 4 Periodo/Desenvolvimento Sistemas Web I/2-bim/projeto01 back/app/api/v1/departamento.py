from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.deps import get_db
## contrato da API - schemas
from app.schemas.departamento import DepartamentoCreate, DepartamentoOut, DepartamentoUpdate
from app.repositories import departamento as repo

rotas = APIRouter(prefix="/v1/Departamento", tags=["Departamento"])

@rotas.post("/", response_model=DepartamentoOut, status_code=status.HTTP_201_CREATED)
def create(payload: DepartamentoCreate, db: Session = Depends(get_db)):
    return repo.create(db, payload)

@rotas.get("/", response_model=list[DepartamentoOut])
def list_all(db: Session = Depends(get_db)):
    return repo.get_all(db)

@rotas.get("/{departamento_id}", response_model=DepartamentoOut)
def get_id(departamento_id: int, db: Session = Depends(get_db)):
    objeto = repo.get(db, departamento_id)
    if not objeto: 
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Departamento não encontrado")
    return objeto

@rotas.put("/{departamento_id}", response_model=DepartamentoOut)
def update(departamento_id: int, payload: DepartamentoUpdate, db: Session = Depends(get_db)):
    objeto = repo.get(db, departamento_id)
    if not objeto:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Departamento não encontrado")
    
    return repo.update(db, departamento_id, payload)

@rotas.delete("/{departamento_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(departamento_id: int, db: Session = Depends(get_db)):
    objeto = repo.get(db, departamento_id)
    if not objeto:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Departamento nao encontrado")
    
    repo.delete(db, departamento_id)
    return None
