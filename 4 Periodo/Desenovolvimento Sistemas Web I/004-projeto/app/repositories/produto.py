from sqlalchemy.orm import Session
#tabela produto
from app.models.produto import Produto
#contrato da APi
from app.schemas.produto import ProdutoCreate, ProdutoUpdate, ProdutoOut


def create(db: Session, produto: ProdutoCreate):
    db_produto = Produto(**produto.dict())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto