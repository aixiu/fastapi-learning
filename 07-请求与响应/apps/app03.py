from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import List, Optional, Union

app03 = APIRouter()

class Addr(BaseModel):
    province: str
    city: str

class User(BaseModel):
    # name: str = Field(pattern="^a")
    name: str
    age: int = Field(default=0, gt=0, lt=100)  # 默认值，大于0，小于100
    birth: Union[date, None] = None # 日期类型 可以为时间也可以为 None
    friends: List[int] = []
    description: Optional[str] = None
    addr: Addr
    
    @field_validator("name")
    def name_must_alpha(cls, value):
        assert value.isalpha(), "name must be alpha"
        return value
    
class Data(BaseModel):
    data: List[User]

    
@app03.post("/user") # 路径参数
# @app02.get("/jobs/{kd}") # 路径参数
async def user(user:User):
    print(user, type(user)) 
    print(user.name, user.birth)
    print(user.model_dump())
    return user

@app03.post("/data") # 路径参数
async def data(data:Data):

    return data