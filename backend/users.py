from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

user_list = [User(id=1, name="Juan", surname="Perez", url="https://www.udemy.com/course/python-3-do-zero-ao-avancado/", age=25),
             User(id=2, name="Maria", surname="Silva", url="https://www.udemy.com/course/python-3-do-zero-ao-avancado/", age=30),
             User(id=3, name="Pedro", surname="Santos", url="https://www.udemy.com/course/python-3-do-zero-ao-avancado/", age=35)]

app = FastAPI()

@app.get("/usersjson")
async def usersjson():
    users = [
        {
            "name": "Juan",
            "age": 25,
            "email": ""
        },
        {
            "name": "Maria",
            "age": 30,
            "email": ""
        },
        {
            "name": "Pedro",
            "age": 35,
            "email": ""
        }
    ]
    return users

@app.get("/users")
async def users():
    return user_list



@app.get("/users/{user_id}")
async def user(user_id: int):
    users_list_2 = filter(lambda user: user.id == user_id, user_list)
    try:
        return list(users_list_2)[0]
    except IndexError:
        return {"message": "User not found"}