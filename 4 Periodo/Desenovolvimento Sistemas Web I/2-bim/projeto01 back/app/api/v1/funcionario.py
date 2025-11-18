from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.funcionario import FuncionarioCreate, FuncionarioUpdate, FuncionarioOut
from app.repositories.funcionario import FuncionarioRepository

router = rotas = APIRouter(prefix="/v1/Funcionario", tags=["Funcionario"])
repo = FuncionarioRepository()

@router.post("/", response_model=FuncionarioOut)
def create_funcionario(payload: FuncionarioCreate, db: Session = Depends(get_db)):
    return repo.create(db, payload)

@router.get("/", response_model=list[FuncionarioOut])
def read_funcionarios(db: Session = Depends(get_db)):
    return repo.get_all(db)

@router.get("/{id}", response_model=FuncionarioOut)
def read_funcionario(id: int, db: Session = Depends(get_db)):
    return repo.get_by_id(db, id)

@router.put("/{id}", response_model=FuncionarioOut)
def update_funcionario(id: int, payload: FuncionarioUpdate, db: Session = Depends(get_db)):
    return repo.update(db, id, payload)

@router.delete("/{id}")
def delete_funcionario(id: int, db: Session = Depends(get_db)):
    return repo.delete(db, id)