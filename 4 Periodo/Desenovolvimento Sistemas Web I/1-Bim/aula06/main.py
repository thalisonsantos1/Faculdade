from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import ProdutoCreate
from schemes import Produto
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/produtos/")
async def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all()

@app.get("/produtos/{prod_id}")
async def lista_produto(prod_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == prod_id).first()
    if not produto:
        return {"error": "Produto nao encontrado"}
    return {
        "id": produto.id,
        "nome": produto.nome,
        "preco": produto.preco
    }

@app.put("/produtos/{prod_id}")
async def editar_produto(prod_id: int, prod: ProdutoCreate, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == prod_id).first()
    if not produto:
        return {"error": "Produto nao encontrado"}
    produto.nome = prod.nome
    produto.preco = prod.preco
    db.commit()
    return {"message": f"Produto com o {id} alterado com sucesso"}

@app.post("/produtos/", status_code=201)
def criar_produto(prod: ProdutoCreate, db: Session = Depends(get_db)):
    novo_prod = Produto(nome=prod.nome, preco=prod.preco)
    db.add(novo_prod)
    db.commit()
    db.refresh(novo_prod)
    return novo_prod

@app.delete("/produtos/{prod_id}", status_code=200)
def excluir(prod_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == prod_id).first()
    if not produto:
        return {"error": "Produto nao encontrado"}
    db.delete(produto)
    db.commit()
    return {"message": f"Produto com o {id} excluido com sucesso"}

