from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/url")
async def url():
    return {"url_curso": "https://www.udemy.com/course/python-3-do-zero-ao-avancado/"}
