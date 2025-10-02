from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models, schemas
from app.db.session import get_db

router = APIRouter(prefix="/estoque", tags=["estoque"])

# ==========================
# Criar movimento de estoque
# ==========================
@router.post("/movimentos", response_model=schemas.EstoqueMovimentoOut, status_code=status.HTTP_201_CREATED)
def criar_movimento(mov: schemas.EstoqueMovimentoCreate, db: Session = Depends(get_db)):
    # Verifica se o produto existe
    produto = db.query(models.Produto).filter(models.Produto.id == mov.produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    movimento = models.EstoqueMovimento(
        produto_id=mov.produto_id,
        tipo=mov.tipo,
        quantidade=mov.quantidade,
        descricao=mov.descricao
    )
    db.add(movimento)
    db.commit()
    db.refresh(movimento)
    return movimento

# ==========================
# Obter saldo de produto
# ==========================
@router.get("/saldo/{produto_id}", response_model=schemas.SaldoOut)
def obter_saldo(produto_id: int, db: Session = Depends(get_db)):
    saldo = db.query(
        func.sum(
            func.case(
                [(models.EstoqueMovimento.tipo == 'entrada', models.EstoqueMovimento.quantidade),
                 (models.EstoqueMovimento.tipo == 'venda', -models.EstoqueMovimento.quantidade),
                 (models.EstoqueMovimento.tipo == 'devolucao', models.EstoqueMovimento.quantidade),
                 (models.EstoqueMovimento.tipo == 'ajuste', models.EstoqueMovimento.quantidade)]
            )
        )
    ).filter(models.EstoqueMovimento.produto_id == produto_id).scalar() or 0

    return {"produto_id": produto_id, "saldo": saldo}

# ==========================
# Registrar venda
# ==========================
@router.post("/venda", response_model=schemas.EstoqueMovimentoOut, status_code=status.HTTP_201_CREATED)
def registrar_venda(produto_id: int, quantidade: int, db: Session = Depends(get_db)):
    # Verifica saldo disponível
    saldo_atual = obter_saldo(produto_id, db)["saldo"]
    if quantidade > saldo_atual:
        raise HTTPException(status_code=400, detail="Saldo insuficiente para venda")

    movimento = models.EstoqueMovimento(
        produto_id=produto_id,
        tipo="venda",
        quantidade=quantidade,
        descricao="Venda realizada"
    )
    db.add(movimento)
    db.commit()
    db.refresh(movimento)
    return movimento

# ==========================
# Registrar devolução
# ==========================
@router.post("/devolucao", response_model=schemas.EstoqueMovimentoOut, status_code=status.HTTP_201_CREATED)
def registrar_devolucao(produto_id: int, quantidade: int, db: Session = Depends(get_db)):
    movimento = models.EstoqueMovimento(
        produto_id=produto_id,
        tipo="devolucao",
        quantidade=quantidade,
        descricao="Devolução registrada"
    )
    db.add(movimento)
    db.commit()
    db.refresh(movimento)
    return movimento

# ==========================
# Registrar ajuste
# ==========================
@router.post("/ajuste", response_model=schemas.EstoqueMovimentoOut, status_code=status.HTTP_201_CREATED)
def registrar_ajuste(mov: schemas.EstoqueMovimentoCreate, db: Session = Depends(get_db)):
    produto = db.query(models.Produto).filter(models.Produto.id == mov.produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    movimento = models.EstoqueMovimento(
        produto_id=mov.produto_id,
        tipo="ajuste",
        quantidade=mov.quantidade,
        descricao=mov.descricao
    )
    db.add(movimento)
    db.commit()
    db.refresh(movimento)
    return movimento