from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.deps import get_db
from app.models.produto import Produto
from app.models.estoque_movimento import EstoqueMovimento, TipoMovimento
from app.schemas.estoque_movimento import EstoqueMovimentoCreate, EstoqueMovimentoResponse
import os

router = APIRouter(prefix="/api/v1/estoque", tags=["Estoque"])

# Configuração para permitir ou não saldo negativo
ALLOW_NEGATIVE_STOCK = os.getenv("ALLOW_NEGATIVE_STOCK", "false").lower() == "true"

@router.post("/movimentos", response_model=EstoqueMovimentoResponse)
def criar_movimento(movimento: EstoqueMovimentoCreate, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == movimento.produto_id, Produto.ativo == True).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado ou inativo.")

    if movimento.quantidade <= 0:
        raise HTTPException(status_code=400, detail="Quantidade deve ser maior que zero.")

    # Calcula saldo atual
    entradas = db.query(func.sum(EstoqueMovimento.quantidade)).filter(
        EstoqueMovimento.produto_id == movimento.produto_id,
        EstoqueMovimento.tipo == TipoMovimento.ENTRADA
    ).scalar() or 0

    saidas = db.query(func.sum(EstoqueMovimento.quantidade)).filter(
        EstoqueMovimento.produto_id == movimento.produto_id,
        EstoqueMovimento.tipo == TipoMovimento.SAIDA
    ).scalar() or 0

    saldo_atual = entradas - saidas

    # Verifica saldo negativo
    if movimento.tipo == TipoMovimento.SAIDA and not ALLOW_NEGATIVE_STOCK and movimento.quantidade > saldo_atual:
        raise HTTPException(status_code=400, detail="Saldo insuficiente para saída.")

    novo_movimento = EstoqueMovimento(
        produto_id=movimento.produto_id,
        tipo=movimento.tipo,
        quantidade=movimento.quantidade,
        observacao=movimento.observacao
    )
    db.add(novo_movimento)
    db.commit()
    db.refresh(novo_movimento)
    return novo_movimento

@router.get("/saldo/{produto_id}")
def saldo_produto(produto_id: int, db: Session = Depends(get_db)):
    entradas = db.query(func.sum(EstoqueMovimento.quantidade)).filter(
        EstoqueMovimento.produto_id == produto_id,
        EstoqueMovimento.tipo == TipoMovimento.ENTRADA
    ).scalar() or 0

    saidas = db.query(func.sum(EstoqueMovimento.quantidade)).filter(
        EstoqueMovimento.produto_id == produto_id,
        EstoqueMovimento.tipo == TipoMovimento.SAIDA
    ).scalar() or 0

    saldo = entradas - saidas
    return {"produto_id": produto_id, "saldo": saldo}


@router.get("/abaixo-minimo")
def produtos_abaixo_minimo(db: Session = Depends(get_db)):
    produtos = db.query(Produto).filter(Produto.ativo == True).all()
    abaixo_minimo = []

    for p in produtos:
        entradas = db.query(func.sum(EstoqueMovimento.quantidade)).filter(
            EstoqueMovimento.produto_id == p.id,
            EstoqueMovimento.tipo == TipoMovimento.ENTRADA
        ).scalar() or 0

        saidas = db.query(func.sum(EstoqueMovimento.quantidade)).filter(
            EstoqueMovimento.produto_id == p.id,
            EstoqueMovimento.tipo == TipoMovimento.SAIDA
        ).scalar() or 0

        saldo = entradas - saidas

        if saldo < p.estoque_minimo:
            abaixo_minimo.append({
                "produto_id": p.id,
                "nome": p.nome,
                "saldo": saldo,
                "estoque_minimo": p.estoque_minimo
            })

    return abaixo_minimo


@router.post("/venda", response_model=EstoqueMovimentoResponse)
def registrar_venda(movimento: EstoqueMovimentoCreate, db: Session = Depends(get_db)):
    movimento.tipo = TipoMovimento.SAIDA
    movimento.observacao = movimento.observacao or "venda"
    return criar_movimento(movimento, db)

@router.post("/devolucao", response_model=EstoqueMovimentoResponse)
def registrar_devolucao(movimento: EstoqueMovimentoCreate, db: Session = Depends(get_db)):
    movimento.tipo = TipoMovimento.ENTRADA
    movimento.observacao = movimento.observacao or "devolucao"
    return criar_movimento(movimento, db)

@router.post("/ajuste", response_model=EstoqueMovimentoResponse)
def registrar_ajuste(movimento: EstoqueMovimentoCreate, db: Session = Depends(get_db)):
    if not movimento.observacao:
        raise HTTPException(status_code=400, detail="Motivo obrigatório para ajuste.")
    return criar_movimento(movimento, db)


@router.get("/extrato/{produto_id}")
def extrato_produto(produto_id: int, limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    movimentos = (
        db.query(EstoqueMovimento)
        .filter(EstoqueMovimento.produto_id == produto_id)
        .order_by(EstoqueMovimento.criado_em.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
    return movimentos


@router.get("/resumo")
def resumo_estoque(db: Session = Depends(get_db)):
    produtos = db.query(Produto).filter(Produto.ativo == True).all()
    resumo = []

    for p in produtos:
        entradas = db.query(func.sum(EstoqueMovimento.quantidade)).filter(
            EstoqueMovimento.produto_id == p.id,
            EstoqueMovimento.tipo == TipoMovimento.ENTRADA
        ).scalar() or 0

        saidas = db.query(func.sum(EstoqueMovimento.quantidade)).filter(
            EstoqueMovimento.produto_id == p.id,
            EstoqueMovimento.tipo == TipoMovimento.SAIDA
        ).scalar() or 0

        saldo = entradas - saidas
        abaixo_minimo = saldo < p.estoque_minimo

        resumo.append({
            "produto_id": p.id,
            "nome": p.nome,
            "saldo": saldo,
            "estoque_minimo": p.estoque_minimo,
            "abaixo_minimo": abaixo_minimo
        })

    return resumo
