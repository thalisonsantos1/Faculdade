from sqlalchemy.orm import Session, joinedload
from app.models.treinamento import Treinamento
from app.schemas.treinamento import TreinamentoCreate, TreinamentoUpdate

def create(db: Session, payload: TreinamentoCreate) -> Treinamento:
    objeto = Treinamento(**payload.model_dump())
    db.add(objeto)
    db.commit()
    db.refresh(objeto)
    return objeto

def get(db: Session, treinamento_id: int) -> Treinamento | None:
    return db.query(Treinamento).options(joinedload(Treinamento.funcionario)).filter(Treinamento.id == treinamento_id).first()

def get_all(db: Session) -> list[Treinamento]:
    return db.query(Treinamento).options(joinedload(Treinamento.funcionario)).order_by(Treinamento.id).all()

def get_by_funcionario(db: Session, funcionario_id: int) -> list[Treinamento]:
    return db.query(Treinamento).options(joinedload(Treinamento.funcionario)).filter(Treinamento.funcionario_id == funcionario_id).all()

def update(db: Session, treinamento_id: int, payload: TreinamentoUpdate) -> Treinamento:
    objeto = db.get(Treinamento, treinamento_id)
    if objeto:
        for field, value in payload.model_dump(exclude_unset=True).items():
            setattr(objeto, field, value)
        db.commit()
        db.refresh(objeto)
    return objeto

def delete(db: Session, treinamento_id: int) -> None:
    objeto = db.get(Treinamento, treinamento_id)
    if objeto:
        db.delete(objeto)
        db.commit()