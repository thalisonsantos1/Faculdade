from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from app.db.database import Base

class MovimentoEstoque(Base):
    __tablename__ = "estoque_movimentos"

    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False) 
    tipo = Column(String, nullable=False)  
    quantidade = Column(Integer, nullable=False)
    data_movimento = Column(DateTime, default=datetime.utcnow)  # registra quando ocorreu
