from sqlalchemy.orm import Session
# tabela Cargo
from app.models.cargo import Cargo
from app.models.departamento import Departamento
from fastapi import HTTPException
# contrato da API
from app.schemas.cargo import CargoCreate, CargoOut, CargoUpdate

def create(db: Session, payload: CargoCreate) -> Cargo:
    # objeto = Cargo(nome=payload.nome, preco=payload.preco,Cargo_id=payload.Cargo_id )
    # ver se categoria existe
    departamento = db.get(Departamento,payload.departamento_id)
    if not departamento:
        raise HTTPException(
            status_code = 400,
            detail="Departamento nao encontrado"
        )
    objeto = Cargo(**payload.model_dump())
    db.add(objeto)
    db.commit()
    db.refresh(objeto)
    return objeto

def get(db: Session, Cargo_id: int) -> Cargo | None:
    return db.get(Cargo, Cargo_id)

def get_all(db: Session) -> list[Cargo]:
    return db.query(Cargo).order_by(Cargo.id).all()