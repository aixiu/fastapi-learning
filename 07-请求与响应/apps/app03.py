from datetime import date
from typing import List, Optional, Union

from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator

app03 = APIRouter()


class Addr(BaseModel):
    province: str
    city: str


class User(BaseModel):
    # name: str = Field(pattern="^a")
    name: str
    age: int = Field(default=0, gt=0, lt=100)  # 默认值，大于0，小于100
    # Field函数的主要用途是提供字段级别的配置，例如默认值、别名、标题、描述、约束等。这些配置可以帮助我们在创建数据模型时更准确地描述数据，并在数据验证时提供更多的信息。
    birth: Union[date, None] = None  # 日期类型 可以为时间也可以为 None
    friends: List[int] = []
    description: Optional[str] = None
    addr: Addr

    @field_validator("name")
    def name_must_alpha(cls, value):
        assert value.isalpha(), "name must be alpha"
        return value


class Data(BaseModel):
    data: List[User]


@app03.post("/user")  # 路径参数
# @app02.get("/jobs/{kd}") # 路径参数
async def user(user: User):
    print(user, type(user))
    print(user.name, user.birth)
    print(user.model_dump())
    return user


@app03.post("/data")  # 路径参数
async def data(data: Data):

    return data
