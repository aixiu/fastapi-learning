from fastapi import APIRouter
from typing import Union, Optional

app02 = APIRouter()


@app02.get("/jobs") # 路径参数
# @app02.get("/jobs/{kd}") # 路径参数
# async def get_jobs(kd, xl: Union[str, None]=None, gj: Optional[str]=None): 
async def get_jobs(kd, xl: str | None=None, gj: Optional[str]=None): 
    # Optional[str] 相当于 Union[str, None]
    # 有没默认值的参数，必须在参数列表中，有默认
    # 基于kd, xl, gj数据库查询岗位信息
    return {
        "kd": kd,
        "xl": xl,
        "gj": gj
    }