import uvicorn
from typing import Optional, Union

from fastapi import FastAPI, Depends, HTTPException

from api.todos.router import todo_api_router
from api.user.router import user_api_router

from database import create_db_and_tables

app = FastAPI()



app.include_router(user_api_router, prefix='/user')
app.include_router(todo_api_router, prefix='/todos')



if __name__ == '__main__':
    uvicorn.run("main2:app", reload=True,port=8088)