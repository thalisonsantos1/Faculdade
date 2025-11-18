from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import date
from app.db.deps import get_db
from app.schemas.treinamento_realizado import TreinamentoRealizadoCreate, TreinamentoRealizadoOut, TreinamentoRealizadoUpdate
from app.repositories import treinamento_realizado as repo

rotas = APIRouter(prefix="/treinamentos-realizados", tags=["Treinamentos Realizados"])

@rotas.post("/", response_model=TreinamentoRealizadoOut, status_code=status.HTTP_201_CREATED)
def criar_treinamento_realizado(treinamento: TreinamentoRealizadoCreate, db: Session = Depends(get_db)):
    try:
        return repo.create(db, treinamento)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@rotas.get("/", response_model=list[TreinamentoRealizadoOut])
def listar_treinamentos_realizados(db: Session = Depends(get_db)):
    return repo.get_all(db)

@rotas.get("/{treinamento_id}", response_model=TreinamentoRealizadoOut)
def buscar_treinamento_realizado(treinamento_id: int, db: Session = Depends(get_db)):
    treinamento = repo.get(db, treinamento_id)
    if not treinamento:
        raise HTTPException(status_code=404, detail="Treinamento realizado não encontrado")
    return treinamento

@rotas.get("/funcionario/{funcionario_id}", response_model=list[TreinamentoRealizadoOut])
def listar_treinamentos_por_funcionario(funcionario_id: int, db: Session = Depends(get_db)):
    return repo.get_by_funcionario(db, funcionario_id)

@rotas.get("/funcionario/{funcionario_id}/validos", response_model=list[TreinamentoRealizadoOut])
def listar_treinamentos_validos_por_funcionario(
    funcionario_id: int, 
    data_referencia: date = Depends(lambda: date.today()),
    db: Session = Depends(get_db)
):
    return repo.get_validos_by_funcionario(db, funcionario_id, data_referencia)

@rotas.put("/{treinamento_id}", response_model=TreinamentoRealizadoOut)
def atualizar_treinamento_realizado(
    treinamento_id: int,
    treinamento: TreinamentoRealizadoUpdate,
    db: Session = Depends(get_db)
):
    updated = repo.update(db, treinamento_id, treinamento)
    if not updated:
        raise HTTPException(status_code=404, detail="Treinamento realizado não encontrado")
    return updated

@rotas.delete("/{treinamento_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_treinamento_realizado(treinamento_id: int, db: Session = Depends(get_db)):
    treinamento = repo.get(db, treinamento_id)
    if not treinamento:
        raise HTTPException(status_code=404, detail="Treinamento realizado não encontrado")
    repo.delete(db, treinamento_id)
    return None