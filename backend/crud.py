from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).filter(models.User.is_active == True).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        firstname=user.firstname,
        lastname=user.lastname,
        address=user.address,
        salary=user.salary
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db_user.is_active = False
        db.commit()
        db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        return None  # ถ้าผู้ใช้ไม่พบ ให้คืนค่า None

    # อัปเดตฟิลด์ที่ได้รับจาก user_update
    if user_update.firstname is not None:
        db_user.firstname = user_update.firstname
    if user_update.lastname is not None:
        db_user.lastname = user_update.lastname
    if user_update.address is not None:
        db_user.address = user_update.address
    if user_update.salary is not None:
        db_user.salary = user_update.salary
    if user_update.is_active is not None:
        db_user.is_active = user_update.is_active

    db.commit()
    db.refresh(db_user)
    return db_user

# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


