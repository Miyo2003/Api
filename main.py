from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

class HelloResponse(BaseModel):
    message: str

@app.get("/hello", response_model=HelloResponse)
def get_hello():
    return HelloResponse(message="Hello World")