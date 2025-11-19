from fastapi import FastAPI
import httpx

#criando o app
app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}
