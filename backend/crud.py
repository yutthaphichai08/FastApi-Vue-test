from datetime import timedelta
from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
import helper
import models, schemas


def get_appli(db: Session, appli_id: int):
    return db.query(models.Application).filter(models.Application.id == appli_id).first()


def get_applis(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Application).filter(models.Application.is_active == True).offset(skip).limit(limit).all()


def create_appli(db: Session, appli: schemas.ApplicationCreate):
    db_appli = models.Application(
        firstname=appli.firstname,
        lastname=appli.lastname,
        address=appli.address,
        salary=appli.salary,
        is_active=appli.is_active
    )
    db.add(db_appli)
    db.commit()
    db.refresh(db_appli)
    return db_appli


def delete_appli(db: Session, appli_id: int):
    db_appli = db.query(models.Application).filter(models.Application.id == appli_id).first()
    if db_appli:
        db_appli.is_active = False
        db.commit()
        db.refresh(db_appli)
    return db_appli


def update_appli(db: Session, appli_id: int, appli_update: schemas.ApplicationUpdate):
    db_appli = db.query(models.Application).filter(models.Application.id == appli_id).first()
    if not db_appli:
        return None  # ถ้าผู้ใช้ไม่พบ ให้คืนค่า None

    # อัปเดตฟิลด์ที่ได้รับจาก appli_update
    if appli_update.firstname is not None:
        db_appli.firstname = appli_update.firstname
    if appli_update.lastname is not None:
        db_appli.lastname = appli_update.lastname
    if appli_update.address is not None:
        db_appli.address = appli_update.address
    if appli_update.salary is not None:
        db_appli.salary = appli_update.salary
    if appli_update.is_active is not None:
        db_appli.is_active = appli_update.is_active

    db.commit()
    db.refresh(db_appli)
    return db_appli

def import_appli(db: Session, applis: List[schemas.ApplicationCreate]): 
     db.query(models.Application).delete()
     db.commit()

     for user in applis:
         db_appli = models.Application(firstname=user[1], lastname=user[2],address=user[3],salary=user[4])
         db.add(db_appli)
         db.commit()
         db.refresh(db_appli)

     all_appli= db.query(models.Application).all()

     return all_appli
 
def login_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Unauthorization")
    if not helper.verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Unauthorization")
    
    access_token_expires = timedelta(minutes=60 * 24 * 1)
    token = helper.create_access_token(user.id, access_token_expires)

    user.jwt = token

    return user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    # print(user.password)
    hashed_password = helper.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()
