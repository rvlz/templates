from sqlalchemy.orm import Session

from . import models, schemas


def create_user(db: Session, data: schemas.UserCreate):
    user = models.User(
        email=data.email,
        username=data.username,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
