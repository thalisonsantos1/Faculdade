from fastapi import FastAPI
from modelos import Produto
from typing import List

app = FastAPI() # instanciar objeto

produtos: List[Produto] = [] # banco de dados em memória

@app.get("/")
def home():

    return {"message": "API no ar!!!"}

@app.post ("/produtos", response_model=Produto)
def adicionar_produto(prod: Produto):
    produtos.append(prod)
    return {"message": "Produto adicionado com sucesso!!!"}

@app.get("/produtos", response_model=List[Produto])
def listar_produtos():
    return produtos

@app.get("/produtos/{id}", response_model=Produto)
def buscar_produto(id: int):
    for prod in produtos:
        if prod.id == id:
            return prod
    #return {"message": "Produto não encontrado"}
    raise HTTPException(status_code=500, detail="Produto não encontrado")