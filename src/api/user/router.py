from fastapi import APIRouter, Depends
from sqlmodel import Session

from api.user.model import UserOut, UserIn, User
from database import get_session

user_api_router = APIRouter()


@user_api_router.post("/", response_model=UserOut)
def create_user(hero: UserIn, session: Session = Depends(get_session)):
    return User.create(hero, session)


@user_api_router.get("/", response_model=list[UserOut])
def read_user(session: Session = Depends(get_session)):
    return User.all(session)


@user_api_router.get("/{user_id}", response_model=UserOut)
def read_user(user_id: int, session: Session = Depends(get_session)):
    return User.by_id(user_id, session)
