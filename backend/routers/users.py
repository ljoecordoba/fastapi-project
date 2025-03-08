from fastapi import APIRouter, HTTPException
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

router = APIRouter(tags=["users"])

@router.get("/usersjson")
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

@router.get("/users")
async def users():
    return user_list


#Path
@router.get("/user/{user_id}")
async def user(user_id: int):
    users_list_2 = filter(lambda user: user.id == user_id, user_list)
    try:
        return list(users_list_2)[0]
    except IndexError:
        return {"error": "User not found"}

#Query        
@router.get("/user/")
async def userquery(id: int):
    return search_user(id)

@router.post("/user/",response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="User already exists")
    else:
        user_list.append(user)
        return user

@router.put("/user/")
async def user(user: User):
    found = False
    for index,saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            found = True
    if not found:
        return {"error": "User not found"}
    else:
        return user
    
@router.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(user_list):
        if saved_user.id == id:
            print("hola")
            del user_list[index]
            found = True
    if not found:
        return {"error": "User not found"}
        
def search_user(id: int):
    users = filter(lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except :
        return {"error": "User not found"}
    
