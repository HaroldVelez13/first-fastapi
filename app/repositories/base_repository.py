from typing import Type, TypeVar, List, Dict, Any, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from app.repositories.exception import DatabaseError, DuplicateEntryError


# Usamos TypeVar para indicar que esta clase es genérica
# T representa cualquier modelo que herede de Base
T = TypeVar('T')




class BaseRepository:
    """
    Repositorio base para manejar operaciones comunes de la base de datos.
    """
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def get_all(self) -> List[T]:
        """Obtiene todos los registros del modelo."""
        stmt = select(self.model)
        return self.db.scalars(stmt).all()

    def get_by_id(self, item_id: int) -> T | None:
        """Obtiene un registro por su ID."""
        stmt = select(self.model).where(self.model.id == item_id)
        return self.db.scalars(stmt).one_or_none()

    def create(self, item_data: Dict[str, Any]) -> T:
        """Crea un nuevo registro."""
        # Se crea una instancia del modelo con los datos proporcionados
        try:
            new_item = self.model(**item_data)
            self.db.add(new_item)
            self.db.commit()
            self.db.refresh(new_item)
            return new_item
        except IntegrityError as e:
            self.db.rollback()
            raise DuplicateEntryError(detail=f"La entrada ya existe. Error: {e.orig}")
        except SQLAlchemyError as e:
            self.db.rollback()
            raise DatabaseError(detail=f"Ocurrió un error de base de datos. Error: {e}")

    def update(self, item_id: int, item_data: Dict[str, Any]) -> T | None:
        """Actualiza un registro por su ID."""
        item = self.get_by_id(item_id)
        if not item:
            return None
            
        try:
            for key, value in item_data.items():
                setattr(item, key, value)
            self.db.commit()
            self.db.refresh(item)
            return item
        except IntegrityError as e:
            self.db.rollback()
            raise DuplicateEntryError(detail=f"No se puede actualizar el registro. La entrada ya existe. Error: {e.orig}")
        except SQLAlchemyError as e:
            self.db.rollback()
            raise DatabaseError(detail=f"Ocurrió un error de base de datos. Error: {e}")

    def delete(self, item_id: int) -> T | None:
        """Elimina un registro por su ID."""
        item = self.get_by_id(item_id)
        if not item:
            raise DuplicateEntryError(detail=f"No se puede eliminar el registro. La entrada no existe. Error: {item_id}")
            
        try:
            self.db.delete(item)
            self.db.commit()
            return item
        except SQLAlchemyError as e:
            self.db.rollback()
            raise DatabaseError(detail=f"Ocurrió un error de base de datos. Error: {e}")
        
    def get_by(self, **filters) -> Optional[T]:
        """
        Obtiene un registro único según los filtros pasados.
        Ejemplo: repo.get_by(email="test@test.com")
        """
        stmt = select(self.model).filter_by(**filters)
        return self.db.scalars(stmt).one_or_none()
    
    def exists_by(self, **filters) -> bool:
        return self.get_by(**filters) is not None