from pydantic import BaseModel

class Produto(BaseModel):
    id: int
    nome: str
    preco: float