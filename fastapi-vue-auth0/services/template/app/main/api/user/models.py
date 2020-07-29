from sqlalchemy import Column, Integer, String, Boolean
from app.main.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String)
    is_active = Column(Boolean, default=True)
