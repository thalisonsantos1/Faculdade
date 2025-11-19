from sqlalchemy.orm import Session
# Tabela departamento
from app.models.departamento import Departamento as departamento
# Contrato da API
from app.schemas.departamento import DepartamentoCreate as departamentoCreate

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

def delete(db: Session, departamento_id: int) -> None:
    objeto = db.get(departamento, departamento_id)
    if objeto:
        db.delete(objeto)  
        db.commit()