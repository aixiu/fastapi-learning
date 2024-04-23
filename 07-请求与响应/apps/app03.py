from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date
from typing import List

app03 = APIRouter()

class User(BaseModel):
    name: str
    age: int
    birth: date
    friends: List[int]
    


@app03.post("/data") # 路径参数
# @app02.get("/jobs/{kd}") # 路径参数
async def data(user:User):
    print(user, type(user)) 
    print(user.name, user.birth)
    print(user.model_dump())
    return user