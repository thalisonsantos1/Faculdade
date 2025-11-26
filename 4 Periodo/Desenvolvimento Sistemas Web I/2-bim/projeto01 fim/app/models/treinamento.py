from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.db.base import Base

class Treinamento(Base):
    __tablename__ = "treinamentos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(500), nullable=True)
    carga_horaria = Column(Float, nullable=False)
    validade_dias = Column(Integer, nullable=False)

    # Relacionamentos
    realizacoes = relationship("TreinamentoRealizado", back_populates="treinamento")

    def __repr__(self):
        return f"<Treinamento {self.nome}>"