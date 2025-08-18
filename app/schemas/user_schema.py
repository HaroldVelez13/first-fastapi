from datetime import date
from pydantic import BaseModel, EmailStr
from typing import List
# Esquema para la creación de un usuario (campos que se esperan en el cuerpo de la petición)
class UserCreate(BaseModel):
    first_name: str
    last_name: str | None = None
    email: EmailStr
    birdth_date: date | None = None

# Esquema para la respuesta (lo que se devuelve al cliente)
class UserBaseResponse(BaseModel):
    id: int
    first_name: str
    last_name: str | None = None
    email: EmailStr
    birdth_date: date | None = None
    
    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    user: UserBaseResponse
    
    class Config:
        orm_mode = True

class UsersResponseList(BaseModel):
    users: List[UserBaseResponse]