from app.db.database import SessionLocal

# Dependência do FastAPI para injetar sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
