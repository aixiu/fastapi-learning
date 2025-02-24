from fastapi import APIRouter
from typing import Union, Optional

app02 = APIRouter()

# 视频https://www.bilibili.com/video/BV1Ya4y1D7et?spm_id_from=333.788.player.switch&vd_source=20f7c1f5f32f90ae92d9428e45039d9b&p=15  6分45秒有讲解
# 路径函数中声明不属于路径参数的其他函数参数时，它们将被自动解释为"查询字符串"参数，就是 url? 之后用&分割的 key-value 键值对。

# @app02.get("/jobs/{kd}") 就是路径参数
# async def get_jobs(kd, xl: str | None=None, gj: Optional[str]=None):   # xl: str | None=None 是查询字符串参数  kd是路径参数




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