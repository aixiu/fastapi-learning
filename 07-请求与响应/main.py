# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2024/04/23 10:52:04

import uvicorn
from apps.app01 import app01
from apps.app02 import app02
from apps.app03 import app03
from apps.app04 import app04
from apps.app05 import app05
from apps.app06 import app06
from apps.app07 import app07
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="FastAPI-Aixiu")

app.mount("/static", StaticFiles(directory="statics"))
# 路由挂载 静态文件 作用是将一个静态文件目录挂载到应用中，使其可以通过URL访问。
# 例如，将一个名为statics的目录挂载到/static路径，那么statics目录中的文件可以通过http://
# localhost:8000/static/文件名 访问。

app.include_router(app01, tags=["01 路径参数"])
app.include_router(app02, tags=["02 查询参数"])
app.include_router(app03, tags=["03 请求体数据"])
app.include_router(app04, tags=["04 form表单数据"])
app.include_router(app05, tags=["05 文件上传"])
app.include_router(app06, tags=["06 Request对象"])
app.include_router(app07, tags=["07 响应参数"])


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
