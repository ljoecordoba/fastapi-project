from fastapi import FastAPI,Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
        "johndoe": {"username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@gmail.com",
        "disabled": False,
        "password": "123456"
        },
        "alice": {"username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@gmail.com",
        "disabled": True,
        "password": "654321"
        },
        "bob": {"username": "bob",
        "full_name": "Bob Brown",
        "email": "bob@gmail.com",
        "disabled": False,
        "password": "123456"
        }        
}


app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="Incorrect username")
    
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    return {"access_token": user.username, "token_type": "bearer"}

def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    return None

