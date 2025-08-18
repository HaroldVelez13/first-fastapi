from typing import List,Optional,Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

# creamos un tipo de variable "cualquiera"
T = TypeVar("T")

# Creamos el esquema del libro
class UserSchema(BaseModel):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    birdth_date: Optional[str] = None
    
    class Config:
        # le especificamos que será para uso de un ORM
        orm_mode = True
        # Colocamos un ejemplo que se mostrará en el SWAGGER
        schema_extra  = {
            "example":
                {
                    "id": 0,
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "john@mail.com",
                    "birdth_date": "1990-01-01"
                }
        }

# Creamos un schema de respuesta
class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T]