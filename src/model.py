from typing import Optional, Union

from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select


class ActiveRecord(SQLModel):
    @classmethod
    def by_id(cls, _id: int, session):
        obj = session.get(cls, _id)
        if obj is None:
            raise HTTPException(status_code=404, detail=f"{cls.__name__} with id {id} not found")
        return obj

    @classmethod
    def all(cls, session):
        return session.exec(select(cls)).all()

    @classmethod
    def create(cls, source: Union[dict, SQLModel], session):
        if isinstance(source, SQLModel):
            obj = cls.from_orm(source)
        # elif isinstance(source, dict):
        elif isinstance(source, dict):
            obj = cls.parse_obj(source)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

    def save(self, session):
        session.add(self)
        session.commit()
        session.refresh(self)