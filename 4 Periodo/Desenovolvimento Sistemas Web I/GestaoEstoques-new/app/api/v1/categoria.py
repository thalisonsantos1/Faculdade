from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.categoria import CategoriaCreate, CategoriaOut
from app.repositories import categoria as repo



rotas = APIRouter(prefix="/v1/categoria", tags=["categoria"])


@rotas.post("/", response_model=CategoriaOut, status_code=status.HTTP_201_CREATED)
def create(payload: CategoriaCreate, db: Session = Depends(get_db)):
    """Cria uma nova categoria"""
    return repo.create(db, payload)


@rotas.get("/", response_model=list[CategoriaOut])
def list_all(db: Session = Depends(get_db)):
    """Lista todas as categorias"""
    return repo.get_all(db)


@rotas.get("/{id}", response_model=CategoriaOut)
def get_id(id: int, db: Session = Depends(get_db)):
    """Busca uma categoria pelo ID"""
    objeto = repo.get(db, id)
    if not objeto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada")
    return objeto
