from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=False,nullable=False)

    produtos = relationship("Produto", back_populates="categoria")