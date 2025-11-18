from sqlalchemy.orm import Session
from datetime import timedelta, date
from app.models import TreinamentoRealizado, Treinamento
from app.schemas.treinamento_realizado import TreinamentoRealizadoCreate, TreinamentoRealizadoUpdate

def create(db: Session, treinamento_realizado: TreinamentoRealizadoCreate):
    # Busca o treinamento para obter os dias de validade
    treinamento = db.query(Treinamento).filter(Treinamento.id == treinamento_realizado.treinamento_id).first()
    if not treinamento:
        raise ValueError("Treinamento não encontrado")
    
    # Calcula a data de validade
    data_validade = treinamento_realizado.data_realizacao + timedelta(days=treinamento.validade_dias)
    
    # Cria o objeto com todos os dados
    db_obj = TreinamentoRealizado(
        **treinamento_realizado.dict(),
        data_validade=data_validade
    )
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get(db: Session, id: int):
    return db.query(TreinamentoRealizado).filter(TreinamentoRealizado.id == id).first()

def get_all(db: Session):
    return db.query(TreinamentoRealizado).all()

def get_by_funcionario(db: Session, funcionario_id: int):
    return db.query(TreinamentoRealizado).filter(TreinamentoRealizado.funcionario_id == funcionario_id).all()

def get_validos_by_funcionario(db: Session, funcionario_id: int, data_referencia: date):
    return db.query(TreinamentoRealizado).filter(
        TreinamentoRealizado.funcionario_id == funcionario_id,
        TreinamentoRealizado.data_validade >= data_referencia
    ).all()

def update(db: Session, id: int, treinamento_realizado: TreinamentoRealizadoUpdate):
    db_obj = get(db, id)
    if not db_obj:
        return None
    
    update_data = treinamento_realizado.dict(exclude_unset=True)
    
    # Se a data de realização foi atualizada, recalcula a data de validade
    if "data_realizacao" in update_data:
        treinamento = db.query(Treinamento).filter(Treinamento.id == db_obj.treinamento_id).first()
        update_data["data_validade"] = update_data["data_realizacao"] + timedelta(days=treinamento.validade_dias)
    
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete(db: Session, id: int):
    db_obj = get(db, id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj