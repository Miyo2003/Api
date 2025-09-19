from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Replace root endpoint with ASCII art
@app.get("/", response_class=PlainTextResponse)
def read_root():
    art = """

    ♥ Hello World♥
 
  ♥♥♥♥♥  
 ♥        
 ♥        
  ♥♥♥♥   
       ♥ 
       ♥ 
 ♥♥♥♥♥♥♥ 

 
   ♥   
   ♥   
   ♥   
   ♥   
   ♥   
   ♥   
   ♥   

 
 ♥♥♥♥♥♥♥
    ♥   
    ♥   
    ♥   
    ♥   
    ♥   
    ♥   

 
 ♥♥♥♥♥♥♥
    ♥   
    ♥   
    ♥   
    ♥   
    ♥   
    ♥   

 
   ♥   
   ♥   
   ♥   
   ♥   
   ♥   
   ♥   
   ♥   

 
 ♥♥♥♥♥  
 ♥    ♥ 
 ♥    ♥ 
 ♥♥♥♥♥  
 ♥ ♥    
 ♥  ♥   
 ♥   ♥  

 
   ♥   
  ♥ ♥  
 ♥   ♥ 
 ♥♥♥♥♥ 
 ♥   ♥ 
 ♥   ♥ 
 ♥   ♥ 

 
   ♥   
   ♥   
   ♥   
   ♥   
   ♥   
   ♥   
   ♥   

 
 ♥     ♥
 ♥♥    ♥
 ♥ ♥   ♥
 ♥  ♥  ♥
 ♥   ♥ ♥
 ♥    ♥♥
 ♥     ♥

 
   ♥   
  ♥ ♥  
 ♥   ♥ 
 ♥♥♥♥♥ 
 ♥   ♥ 
 ♥   ♥ 
 ♥   ♥ 

 
 ♥     ♥
 ♥♥   ♥♥
 ♥ ♥ ♥ ♥
 ♥  ♥  ♥
 ♥     ♥
 ♥     ♥
 ♥     ♥

 
   ♥   
  ♥ ♥  
 ♥   ♥ 
 ♥♥♥♥♥ 
 ♥   ♥ 
 ♥   ♥ 
 ♥   ♥ 

 
 ♥      
 ♥      
 ♥      
 ♥      
 ♥      
 ♥      
 ♥♥♥♥♥♥♥

 
   ♥   
  ♥ ♥  
 ♥   ♥ 
 ♥♥♥♥♥ 
 ♥   ♥ 
 ♥   ♥ 
 ♥   ♥ 

 
 ♥     ♥
 ♥♥    ♥
 ♥ ♥   ♥
 ♥  ♥  ♥
 ♥   ♥ ♥
 ♥    ♥♥
 ♥     ♥
"""
    return art

# Keep your HelloResponse as is
class HelloResponse(BaseModel):
    message: str

@app.get("/hello", response_model=HelloResponse)
def get_hello():
    return HelloResponse(message="Hello World")


# You can run this app with:
# uvicorn main:app --reload
