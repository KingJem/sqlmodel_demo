from typing import Optional, Union

from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select

from src.model import ActiveRecord


class UserBase(SQLModel):
    name: Optional[str] = None
    age: Optional[int] = None


class User(UserBase, ActiveRecord, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    __table_args__ = {'extend_existing': True}


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    id: int


class UserUpdate(UserBase):
    pass
