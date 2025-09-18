from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class HelloResponse(BaseModel):
    message: str

@app.get("/hello", response_model=HelloResponse)
def get_hello():
    return HelloResponse(message="Hello World")

# You can run this app with:
# uvicorn main:app --reload
