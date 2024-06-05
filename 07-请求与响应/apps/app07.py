from fastapi import APIRouter, Form, File, UploadFile, Request
from pydantic import BaseModel, Field, field_validator, EmailStr
from datetime import date
from typing import List, Optional, Union
from pathlib import Path


app07 = APIRouter()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None
    
class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None
    
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: list[str] = []
    
items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app07.post("/user02", response_model=UserOut)
async def create_user(user: UserIn):
    # 存到数据库
    return user

@app07.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]


# response_model_exclude
@app07.get("/items1/{item_id}", response_model=Item, response_model_exclude={"description"}, )
async def read_item(item_id: str):
    return items[item_id]

# response_model_include  
@app07.get("/items2/{item_id}", response_model=Item, response_model_include={"name", "price"}, )
async def read_item(item_id: str):
    return items[item_id]

# 使用路径操作装饰器的 response_model 参数来定义响应模型，特别是确保私有数据被过滤掉。使用 response_model_exclude_unset 来仅返回显式设定的值。
# 除了response_model_exclude_unset以外，还有response_model_exclude_defaults和response_model_exclude_none，我们可以很直观的了解到他们的意思，不返回是默认值的字段和不返回是None的字段。