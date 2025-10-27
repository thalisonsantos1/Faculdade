from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base 

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)

    categoria_id = Column(
        Integer,
        ForeignKey("categorias.id", ondelete="CASCADE"),
        nullable=False
    )

    categoria = relationship("Categoria", back_populates="produtos")

    estoque_minimo = Column(Integer, default=0)
    ativo = Column(Boolean, default=True)
