from sqlalchemy.orm import Session
from fastapi import HTTPException
# Tabela departamento
from app.models.departamento import Departamento as departamento
# Contrato da API
from app.schemas.departamento import DepartamentoCreate as departamentoCreate, DepartamentoUpdate as departamentoUpdate

def create(db:Session, payload: departamentoCreate) -> departamento:
    objeto = departamento(**payload.model_dump())
    # objeto.nome = payload.nome
    db.add(objeto)
    db.commit()
    db.refresh(objeto)
    return objeto

def get(db: Session, departamento_id: int) -> departamento | None:
    return db.get(departamento, departamento_id)

def get_all(db: Session) -> list[departamento]:
    return db.query(departamento).order_by(departamento.id).all()

def update(db: Session, departamento_id: int, payload: departamentoUpdate) -> departamento:
    objeto = db.get(departamento, departamento_id)
    if not objeto:
        raise HTTPException(
            status_code=404,
            detail="Departamento não encontrado"
        )
    
    # Atualizar apenas os campos que foram fornecidos
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(objeto, key, value)
    
    db.commit()
    db.refresh(objeto)
    return objeto

def delete(db: Session, departamento_id: int) -> None:
    objeto = db.get(departamento, departamento_id)
    if not objeto:
        raise HTTPException(
            status_code=404,
            detail="Departamento não encontrado"
        )
    db.delete(objeto)  
    db.commit()