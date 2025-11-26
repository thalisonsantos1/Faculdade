from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.deps import get_db
from app.models import Treinamento
from app.schemas import TreinamentoCreate, TreinamentoUpdate

rotas = APIRouter(prefix="/treinamentos", tags=["Treinamentos"])

@rotas.post("/")
def criar_treinamento(treinamento: TreinamentoCreate, db: Session = Depends(get_db)):
    db_treinamento = Treinamento(**treinamento.dict())
    db.add(db_treinamento)
    db.commit()
    db.refresh(db_treinamento)
    return db_treinamento

@rotas.get("/")
def listar_treinamentos(db: Session = Depends(get_db)):
    treinamentos = db.query(Treinamento).all()
    return treinamentos

@rotas.get("/{treinamento_id}")
def buscar_treinamento(treinamento_id: int, db: Session = Depends(get_db)):
    treinamento = db.query(Treinamento).filter(Treinamento.id == treinamento_id).first()
    if not treinamento:
        raise HTTPException(status_code=404, detail="Treinamento não encontrado")
    return treinamento

@rotas.put("/{treinamento_id}")
def atualizar_treinamento(treinamento_id: int, treinamento_update: TreinamentoUpdate, db: Session = Depends(get_db)):
    treinamento = db.query(Treinamento).filter(Treinamento.id == treinamento_id).first()
    if not treinamento:
        raise HTTPException(status_code=404, detail="Treinamento não encontrado")
    
    for field, value in treinamento_update.dict(exclude_unset=True).items():
        setattr(treinamento, field, value)
    
    db.commit()
    db.refresh(treinamento)
    return treinamento

@rotas.delete("/{treinamento_id}")
def deletar_treinamento(treinamento_id: int, db: Session = Depends(get_db)):
    treinamento = db.query(Treinamento).filter(Treinamento.id == treinamento_id).first()
    if not treinamento:
        raise HTTPException(status_code=404, detail="Treinamento não encontrado")
    
    db.delete(treinamento)
    db.commit()
    return {"message": "Treinamento deletado com sucesso"}