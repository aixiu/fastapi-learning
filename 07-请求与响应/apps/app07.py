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

@app07.post("/user02")
async def create_user(user: UserIn):
    # 存到数据库
    return user