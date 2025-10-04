from http import HTTPStatus

from fastapi import FastAPI

# from fastapi.responses import HTMLResponse
from fast_zero.schemas import Message, UserDB, UserPublic, UserSchema, UserList

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root() -> dict[str, str]:
    return {'message': 'Hello World'}


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema) -> UserPublic:
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id

@app.get('/users', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}
