from fastapi import FastAPI
from app.routes.user import user
from app.models.create_tables import create_all_tables

create_all_tables()
app = FastAPI(
    title="FastAPI CRUD Ejemplo",
    description="Un ejemplo de aplicación CRUD con FastAPI",
    version="1.0.0"
)

@app.get("/")
def index():
    return {
        "msg":"Hola al crud de usuarios con FastAPI",
    }

app.include_router(user, prefix="/users", tags=["users"])