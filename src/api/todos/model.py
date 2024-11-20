from datetime import datetime
from typing import Optional, Union

from sqlmodel import Field, Session, SQLModel, create_engine, select

from src.model import ActiveRecord


class TodoBase(SQLModel):
    content: Optional[str] = None
    is_done: Optional[int] = None

class TodoIn(TodoBase):
    pass


class TodoOut(TodoBase):
    id: int


class TodoUpdate(TodoBase):
    pass




class Todo(TodoBase, ActiveRecord, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(default='')
    is_done: int = Field()
    __table_args__ = {'extend_existing': True}


