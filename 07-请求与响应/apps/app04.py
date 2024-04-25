from fastapi import APIRouter, Form
from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import List, Optional, Union


app04 = APIRouter()

@app04.post("/regin")
async def reg(username:str=Form(), password:str=Form()):
    print(f"username: {username}, password: {password}")
    # 注册，实现用户名和密码的数据库添加
    return {
        "username": username,
        "password": password
    }