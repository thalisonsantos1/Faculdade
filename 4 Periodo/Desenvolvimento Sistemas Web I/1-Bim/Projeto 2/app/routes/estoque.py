from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import produto, estoque
from app.schemas import estoque_schemas

router = APIRouter(prefix="/api/v1/estoque", tags=["estoque"])

@router.post("/movimentos", response_model=estoque_schemas.EstoqueMovimentoOut)
def criar_movimento(
    movimento: estoque_schemas.EstoqueMovimentoCreate, 
    db: Session = Depends(get_db)
):
    # Verificar se produto existe
    produto_db = db.query(produto.Produto).filter(produto.Produto.id == movimento.produto_id).first()
    if not produto_db:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    # Verificar se produto está ativo
    if not produto_db.ativo:
        raise HTTPException(status_code=400, detail="Produto não está ativo")
    
    # Criar movimento
    db_movimento = estoque.EstoqueMovimento(
        produto_id=movimento.produto_id,
        tipo=movimento.tipo,
        quantidade=movimento.quantidade,
        motivo=movimento.motivo
    )
    
    db.add(db_movimento)
    db.commit()
    db.refresh(db_movimento)
    
    return db_movimento

@router.get("/saldo/{produto_id}", response_model=estoque_schemas.SaldoOut)
def obter_saldo(produto_id: int, db: Session = Depends(get_db)):
    # Verificar se produto existe
    produto_db = db.query(produto.Produto).filter(produto.Produto.id == produto_id).first()
    if not produto_db:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    # Calcular saldo (somatório ENTRADAS - somatório SAÍDAS)
    movimentos = db.query(estoque.EstoqueMovimento).filter(
        estoque.EstoqueMovimento.produto_id == produto_id
    ).all()
    
    saldo = 0
    for mov in movimentos:
        if mov.tipo == estoque_schemas.TipoMovimento.ENTRADA:
            saldo += mov.quantidade
        else:
            saldo -= mov.quantidade
    
    return estoque_schemas.SaldoOut(produto_id=produto_id, saldo=saldo)