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

def update(db: Session, cargo_id: int, payload: CargoUpdate) -> Cargo:
    objeto = db.get(Cargo, cargo_id)
    if not objeto:
        raise HTTPException(
            status_code=404,
            detail="Cargo não encontrado"
        )
    
    # Validar departamento se foi alterado
    if payload.departamento_id:
        departamento = db.get(Departamento, payload.departamento_id)
        if not departamento:
            raise HTTPException(
                status_code=400,
                detail="Departamento não encontrado"
            )
    
    # Atualizar apenas os campos que foram fornecidos
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(objeto, key, value)
    
    db.commit()
    db.refresh(objeto)
    return objeto

def delete(db: Session, cargo_id: int) -> None:
    objeto = db.get(Cargo, cargo_id)
    if not objeto:
        raise HTTPException(
            status_code=404,
            detail="Cargo não encontrado"
        )
    db.delete(objeto)
    db.commit()