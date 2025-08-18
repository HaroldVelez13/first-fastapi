from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    nombre: str
    apellido: str

app = FastAPI()


@app.get("/")
def index():
    return {"saludo": f"Hola Mundo"}


@app.get("/juego")
async def game():
    return {"saludo": "Hola al juego"}


@app.get("/juego/option/{opcion}")
async def game_option(opcion: str):
    return {"opcion": f"{opcion}"}