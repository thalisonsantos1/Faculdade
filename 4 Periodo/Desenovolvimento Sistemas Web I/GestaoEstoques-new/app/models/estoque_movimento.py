from sqlalchemy import Column, Integer, Enum, ForeignKey, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.database import Base
import enum

class TipoMovimento(str, enum.Enum):
    ENTRADA = "entrada"
    SAIDA = "saida"

class EstoqueMovimento(Base):
    __tablename__ = "estoque_movimentos"

    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("produtos.id", ondelete="CASCADE"), nullable=False)
    tipo = Column(Enum(TipoMovimento), nullable=False)
    quantidade = Column(Integer, nullable=False)
    observacao = Column(String, nullable=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
