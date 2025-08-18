from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.user_model import UserModel
from app.schemas.user_schema import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[UserModel]:
        """Obtiene todos los usuarios de la base de datos."""
        return self.db.scalars(select(UserModel)).all()

    def get_by_id(self, user_id: int) -> UserModel | None:
        """Obtiene un usuario por su ID."""
        return self.db.scalars(select(UserModel).where(UserModel.id == user_id)).one_or_none()

    def create(self, user: UserCreate) -> UserModel:
        """Crea un nuevo usuario en la base de datos."""
        _user = UserModel(**user.dict())
        self.db.add(_user)
        self.db.commit()
        self.db.refresh(_user)
        return _user

    def update(self, user_id: int, user: UserCreate) -> UserModel | None:
        """Actualiza un usuario existente."""
        _user = self.get_by_id(user_id)
        if _user:
            # Actualiza los campos uno por uno para mayor claridad y seguridad
            _user.first_name = user.first_name
            _user.last_name = user.last_name
            _user.email = user.email
            _user.birdth_date = user.birdth_date
            self.db.commit()
            self.db.refresh(_user)
        return _user

    def delete(self, user_id: int) -> str | None:
        """Elimina un usuario por su ID."""
        _user = self.get_by_id(user_id)
        if _user:
            self.db.delete(_user)
            self.db.commit()
        return f"Usuario con ID {user_id} eliminado" if _user else None
    
    def check_email(self, email: str) -> bool:
        """Verifica si un email ya existe en la base de datos."""
        return self.db.scalars(select(UserModel).where(UserModel.email == email)).one_or_none() is not None