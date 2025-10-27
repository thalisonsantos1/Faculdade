from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Produto(Base):
    __tablename__ = "produtos"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)
    preco = Column(Integer)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    estoque_minimo = Column(Integer, default=0)
    ativo = Column(Boolean, default=True)
    
    categoria = relationship("Categoria", back_populates="produtos")
    movimentos = relationship("EstoqueMovimento", back_populates="produto")