from sqlalchemy.orm import Session # La sesión de la DB
from app.models.user_model import UserModel # El modelo ORM de nuestra DB
from app.schemas.user_schema import UserSchema # el esquema del JSON



def get_users(db: Session):
    _users = db.query(UserModel).all()   
    return _users  

def get_user_paginate(db:Session, skip:int=0, limit:int=100):
    return db.query(UserModel).offset(skip).limit(limit).all()

def get_user(db:Session,user_id:int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()

def create_user(db:Session, user:UserSchema):
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

def delete_user(db:Session, user_id:int):
    _user = get_user(db=db,user_id=user_id)
    db.delete(_user)
    db.commit()
    return _user
