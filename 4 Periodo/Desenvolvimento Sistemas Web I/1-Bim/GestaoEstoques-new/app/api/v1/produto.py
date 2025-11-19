from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.produto import ProdutoCreate, ProdutoOut
from app.repositories import produto as repo
from app.models.estoque_movimento import EstoqueMovimento, TipoMovimento
from app.models.produto import Produto

rotas = APIRouter(prefix="/v1/produto", tags=["produto"])


@rotas.post("/", response_model=ProdutoOut, status_code=status.HTTP_201_CREATED)
def create(payload: ProdutoCreate, db: Session = Depends(get_db)):
    """Cria um novo produto"""
    return repo.create(db, payload)


@rotas.get("/", response_model=list[ProdutoOut])
def list_all(db: Session = Depends(get_db)):
    """Lista todos os produtos"""
    return repo.get_all(db)


@rotas.get("/{id}", response_model=ProdutoOut)
def get_id(id: int, db: Session = Depends(get_db)):
    """Busca um produto pelo ID"""
    objeto = repo.get(db, id)
    if not objeto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    return objeto


# Função para calcular saldo
def calcular_saldo(produto_id: int, db: Session) -> int:
    entradas = db.query(EstoqueMovimento).filter(
        EstoqueMovimento.produto_id == produto_id,
        EstoqueMovimento.tipo == TipoMovimento.ENTRADA
    ).all()
    saidas = db.query(EstoqueMovimento).filter(
        EstoqueMovimento.produto_id == produto_id,
        EstoqueMovimento.tipo == TipoMovimento.SAIDA
    ).all()
    return sum(e.quantidade for e in entradas) - sum(s.quantidade for s in saidas)


#  Listar produtos abaixo do estoque mínimo
@rotas.get("/abaixo-minimo")
def produtos_abaixo_minimo(db: Session = Depends(get_db)):
    """Lista produtos com saldo abaixo do estoque mínimo"""
    produtos = db.query(Produto).filter(Produto.ativo == True).all()

    resultado = []
    for p in produtos:
        saldo = calcular_saldo(p.id, db)
        if saldo < p.estoque_minimo:
            resultado.append({
                "produto_id": p.id,
                "nome": p.nome,
                "saldo": saldo,
                "estoque_minimo": p.estoque_minimo,
            })

    return resultado
