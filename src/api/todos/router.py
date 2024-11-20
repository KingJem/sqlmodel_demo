from fastapi import APIRouter, Depends
from sqlmodel import Session

from api.todos.model import TodoBase,TodoIn,TodoOut,TodoUpdate,Todo
from database import get_session

todo_api_router = APIRouter()


@todo_api_router.post("/", response_model=TodoOut)
def create_todo(hero: TodoIn, session: Session = Depends(get_session)):
    return Todo.create(hero, session)


@todo_api_router.get("/", response_model=list[Todo])
def read_todo(session: Session = Depends(get_session)):
    return Todo.all(session)


@todo_api_router.get("/{_id}", response_model=Todo)
def read_todo(_id: int, session: Session = Depends(get_session)):
    return Todo.by_id(_id, session)
