from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Funcionario(Base):
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cargo_id = Column(
        Integer, 
        ForeignKey("cargos.id", ondelete="CASCADE"),
        nullable=False
    )
    
    # Relacionamentos
    cargo = relationship("Cargo", back_populates="funcionarios")
    treinamentos_realizados = relationship("TreinamentoRealizado", back_populates="funcionario")