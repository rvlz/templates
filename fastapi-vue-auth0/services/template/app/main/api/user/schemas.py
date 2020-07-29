from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: Optional[str] = None


class UserCreate(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
