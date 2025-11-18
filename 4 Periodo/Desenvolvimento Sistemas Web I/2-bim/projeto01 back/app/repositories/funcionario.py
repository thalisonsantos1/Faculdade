from sqlalchemy.orm import Session
from app.models.funcionario import Funcionario
from app.schemas.funcionario import FuncionarioCreate, FuncionarioUpdate

class FuncionarioRepository:
    def create(self, db: Session, payload: FuncionarioCreate):
        # Converte para dicionário
        dados = payload.model_dump()
        
        # Remove campos que não existem no modelo
        campos_validos = [column.name for column in Funcionario.__table__.columns]
        dados_filtrados = {k: v for k, v in dados.items() if k in campos_validos}
        
        objeto = Funcionario(**dados_filtrados)
        db.add(objeto)
        db.commit()
        db.refresh(objeto)
        return objeto
    
    def get_all(self, db: Session):
        return db.query(Funcionario).all()
    
    def get_by_id(self, db: Session, id: int):
        return db.query(Funcionario).filter(Funcionario.id == id).first()
    
    def update(self, db: Session, id: int, payload: FuncionarioUpdate):
        objeto = db.query(Funcionario).filter(Funcionario.id == id).first()
        if objeto:
            update_data = payload.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                if hasattr(objeto, field):
                    setattr(objeto, field, value)
            db.commit()
            db.refresh(objeto)
        return objeto
    
    def delete(self, db: Session, id: int):
        objeto = db.query(Funcionario).filter(Funcionario.id == id).first()
        if objeto:
            db.delete(objeto)
            db.commit()
        return objeto