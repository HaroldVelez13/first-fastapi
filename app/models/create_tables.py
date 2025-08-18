from app.config.db import Base, engine
from app.models.user_model import UserModel

def create_all_tables():
    print("Iniciando la creación de tablas en la base de datos...")

    Base.metadata.create_all(bind=engine)

    print("¡Tablas creadas con éxito!")