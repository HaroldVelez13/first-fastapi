
from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from app.config.db import SessionLocal,get_db
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserSchema, Response

from app.crud import user as user_crud

# Creamos un router, que es un conjunto de rutas agrupadas
user = APIRouter()

# Cabe mencionar que vamos a usar constantemente dos parametros 
# "request" el cual es la entrada y será acorde con el esquema "mostrar en SWAGGER"
# y "db" que es de tipo Sesion y de la cual depende de la conexión de nuestr db

# haremos uso de las funciones que creamos en el archivo de user_crud.py

# Creamos la ruta con la que crearemos 
@user.post("/")
async def create_user(request: UserSchema, db: Session = Depends(get_db)):
    user_crud.create_user(db, user=request)
    print(request)
    return Response(status="Ok",
                    code="200",
                    message="User created successfully",result=request).dict(exclude_none=True)
    # retornamos la respuesta con el schema de response


@user.get("/")
async def get_users( db: Session = Depends(get_db)):
    _users = user_crud.get_users(db)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_users)


@user.put("/{user_id}")
async def update_user(user_id:int, request: UserSchema, db: Session = Depends(get_db)):
    try:
        data = request.dict(exclude_unset=True)
        id = user_id
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        birdth_date = data.get("birdth_date")
        _user = user_crud.update_user(db, 
                                      user_id=id,
                                        first_name=first_name,
                                        last_name=last_name,
                                        email=email,
                                        birdth_date=birdth_date)
        return Response(status="Ok", code="200", message="Success update data", result=_user)
    except Exception as e:
        return Response(
            status="bad",
            code="304",
            message="the updated gone wrong"
        )
    # colocamos una excepción por si ocurre un error en la escritura en la db


@user.delete("/{user_id}")
async def delete_user(user_id:int,  db: Session = Depends(get_db)):
    try:
        user_crud.delete_user(db, user_id=user_id)
        return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
    except Exception as e:
        return Response(
            status="bad",
            code="",
            message="the deleted gone wrong"
        )
    # colocamos una excepción por si ocurre un error en la escritura en la db