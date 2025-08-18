from sqlalchemy import Column, Integer, String, Date
from app.config.db import Base

# clase UserModel que hereda de Base
class UserModel(Base):

    # nombre de la tabla
    __tablename__ = "users"    

    # Las columnas de nuestra tabla y el tipo de dato de cada una
    id = Column(Integer, primary_key=True) #Clave primaria

    first_name = Column(String(50), nullable=False) #Nombre: No puede ser nulo

    last_name = Column(String(150), nullable=True) #Apellido: Puede ser nulo

    email = Column(String(80), unique=True, nullable=False) #Email: No puede ser nulo y debe ser único
    
    birdth_date = Column(Date(), nullable=True)  #Fecha de nacimiento: Puede ser nulo, Formato: YYYY-MM-DD (Año, Mes, Día)