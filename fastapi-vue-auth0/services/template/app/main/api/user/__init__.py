from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import schemas, utils, dependencies as deps
from app.main.database import get_db
from app.main.exceptions import EmailTakenException, UserNotFoundException

router = APIRouter()


@router.post("/self", response_model=schemas.User)
def create_current_user(
    data: schemas.UserCreate,
    email: str = Depends(deps.get_current_user_email(verify=False)),
    db: Session = Depends(get_db),
):
    user = utils.get_user_by_email(db, email)
    if user:
        raise EmailTakenException()
    data.email = email
    user = utils.create_user(db, data)
    return user


@router.get("/self", response_model=schemas.User)
def get_current_user(
    email: str = Depends(deps.get_current_user_email(verify=False)),
    db: Session = Depends(get_db),
):
    user = utils.get_user_by_email(db, email)
    if user is None:
        raise UserNotFoundException()
    return user
