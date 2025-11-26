from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import date, timedelta

class TreinamentoRealizado(Base):
    __tablename__ = "treinamentos_realizados"

    id = Column(Integer, primary_key=True, index=True)
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"), nullable=False)
    treinamento_id = Column(Integer, ForeignKey("treinamentos.id"), nullable=False)
    data_realizacao = Column(String, nullable=False)  # Armazenado como string ISO (YYYY-MM-DD)
    data_validade = Column(String, nullable=False)  # Armazenado como string ISO (YYYY-MM-DD)

    # Relacionamentos
    funcionario = relationship("Funcionario", back_populates="treinamentos_realizados")
    treinamento = relationship("Treinamento", back_populates="realizacoes")

    def __repr__(self):
        return f"<TreinamentoRealizado {self.treinamento_id} - {self.funcionario_id}>"