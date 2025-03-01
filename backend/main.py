from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/url")
async def url():
    return {"url_curso": "https://www.udemy.com/course/python-3-do-zero-ao-avancado/"}

#Inicia el server: uvicorn main:app --reload
#Detener el server: Ctrl + C

#Documentacion con Swagger: http://127.0.0.1:8000/docs
#Documentacion con ReDocly: http://127.0.0.1:8000/redoc