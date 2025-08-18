from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.schemas.user_schema import UserCreate, UserResponse, UsersResponseList
from app.repositories.user_repository import UserRepository
from sqlalchemy.exc import IntegrityError
from app.repositories.exception import DuplicateEntryError

# Crear el router para las rutas de usuario
user = APIRouter()



# Definir las rutas
@user.get("/", response_model=UsersResponseList)
def get_all_users(db: Session = Depends(get_db)):
    """Obtiene una lista de todos los usuarios."""
    user_repo = UserRepository(db)
    _users = user_repo.get_all()
    return {"users": _users}

@user.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """Obtiene un solo usuario por su ID."""
    user_repo = UserRepository(db)
    user = user_repo.get_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return {"user":user}

@user.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    """Crea un nuevo usuario."""
    user_repo = UserRepository(db)
    # Verificar si el email ya existe
    if user_repo.check_email(user.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail= f"El email {user.email} ya está en uso",
        )
    try:
        new_user = user_repo.create(user)
        return {"user":new_user}
    
    except IntegrityError as e:   
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error al crear el usuario"
        )
    

@user.put("/{user_id}", response_model=UserResponse)
def update_user_by_id(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    """Actualiza un usuario existente."""
    user_repo = UserRepository(db)
    updated_user = user_repo.update(user_id, user)
    if not updated_user:
        raise DuplicateEntryError(
            detail="Usuario no encontrado"
        )
    return {"user":updated_user}

@user.delete("/{user_id}")
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """Elimina un usuario."""
    user_repo = UserRepository(db)
    deleted_user = user_repo.delete(user_id)
    if not deleted_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return {"detail":deleted_user}