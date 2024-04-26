# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2024/04/26 18:13:58

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2024/04/23 10:52:04

from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/index")
def index(request:Request):
    name = "root"
    return templates.TemplateResponse(
        "index.html", # 模板文件
        {   
            "request": request,
            "user": name
        }, # context上下文对象，一个字典
    )


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)