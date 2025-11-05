from pydantic import BaseModel
from typing import Optional

class ProdutoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: int
    categoria_id: int
    estoque_minimo: int = 0
    ativo: bool = True

class ProdutoCreate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    id: int
    
    class Config:
        from_attributes = True