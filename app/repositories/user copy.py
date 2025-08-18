from sqlalchemy.orm import Session # La sesión de la DB
from app.models.user_model import UserModel # El modelo ORM de nuestra DB
from app.schemas.user_schema import UserSchema # el esquema del JSON

""" 
    CRUD de usuarios
    Este archivo contiene las funciones CRUD para manejar los usuarios en la base de datos.
    Estas funciones permiten crear, leer, actualizar y eliminar usuarios.
    Cada función recibe una sesión de la base de datos y los parámetros necesarios para realizar la operación.
    Las funciones devuelven los resultados correspondientes, ya sea un usuario, una lista de usuarios o un mensaje de éxito o error.
"""

""" 
get_users: Obtiene todos los usuarios de la base de datos.
Parámetros:
- db: La sesión de la base de datos.
Retorna:
- Una lista de objetos UserModel que representan a todos los usuarios en la base de datos.
Uso:
db: La sesión de la base de datos.
query: Realiza una consulta a la base de datos.
all: Trae todos los resultados.
"""
def get_users(db: Session):
    _users = db.query(UserModel).all()   
    return _users  


"""get_user_paginate: Obtiene una lista paginada de usuarios de la base de datos.
Parámetros:
- db: La sesión de la base de datos.
- skip: El número de usuarios a omitir (paginación).
- limit: El número máximo de usuarios a retornar.
Retorna:
- Una lista de objetos UserModel que representan a los usuarios paginados.
Uso:
db: La sesión de la base de datos.
query: Realiza una consulta a la base de datos.
offset: Omite el número de usuarios especificado por skip.
limit: Limita el número de usuarios retornados a la cantidad especificada por limit.
"""
def get_user_paginate(db:Session, skip:int=0, limit:int=100):
    return db.query(UserModel).offset(skip).limit(limit).all()


"""
get_user: Obtiene un usuario específico de la base de datos por su ID.
Parámetros:
- db: La sesión de la base de datos.
- user_id: El ID del usuario a buscar.
Retorna:
- Un objeto UserModel que representa al usuario encontrado, o None si no se encuentra.
Uso:
db: La sesión de la base de datos.
query: Realiza una consulta a la base de datos.
filter: Filtra los resultados según el ID del usuario.
first: Devuelve el primer resultado encontrado o None si no hay resultados.
"""   
def get_user(db:Session,user_id:int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


"""create_user: Crea un nuevo usuario en la base de datos.
Parámetros:
- db: La sesión de la base de datos.
- user: Un objeto UserSchema que contiene los datos del usuario a crear.
Retorna:        
- Un objeto UserModel que representa al usuario creado.
Uso:    
db: La sesión de la base de datos.
user: Un objeto UserSchema con los datos del nuevo usuario.
add: Agrega el nuevo usuario a la sesión de la base de datos.
commit: Guarda los cambios en la base de datos.
refresh: Actualiza el objeto con los datos de la base de datos.
"""
def create_user(db:Session, user:UserSchema):
    print("***********************")
    print("Creando usuario:", user)
    _user = UserModel(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        birdth_date=user.birdth_date
    )
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


"""update_user: Actualiza un usuario existente en la base de datos.
Parámetros:                     
- db: La sesión de la base de datos.
- user_id: El ID del usuario a actualizar.
- title: El nuevo título del usuario.
- description: La nueva descripción del usuario.
Retorna:        
- Un objeto UserModel que representa al usuario actualizado.
Uso:
db: La sesión de la base de datos.
user_id: El ID del usuario a actualizar.
get_user: Obtiene el usuario existente por su ID.
Reasigna los valores de los campos title y description del usuario.
commit: Guarda los cambios en la base de datos.
refresh: Actualiza el objeto con los datos de la base de datos.
"""
def update_user(db:Session, user_id:int,
                first_name:str, 
                last_name:str, 
                email:str,
                birdth_date:str):
    _user = get_user(db=db, user_id=user_id)
    _user.first_name = first_name
    _user.last_name = last_name
    _user.email = email,
    _user.birdth_date = birdth_date
    db.commit()
    db.refresh(_user)
    return _user

"""delete_user: Elimina un usuario de la base de datos por su ID.
Parámetros:
- db: La sesión de la base de datos.
- user_id: El ID del usuario a eliminar.
Retorna:    
- Un objeto UserModel que representa al usuario eliminado.
Uso:
db: La sesión de la base de datos.
get_user: Obtiene el usuario existente por su ID.
delete: Elimina el usuario de la sesión de la base de datos.
commit: Guarda los cambios en la base de datos.
"""
def delete_user(db:Session, user_id:int):
    _user = get_user(db=db,user_id=user_id)
    db.delete(_user)
    db.commit()
    return _user
