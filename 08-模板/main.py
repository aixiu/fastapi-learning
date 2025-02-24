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
    age = 32
    
    books =  ["金瓶梅", "聊斋", "剪灯新话", "国色天香"]
    
    info = {"name": "rain", "age":32, "gender": "male"}
    
    pai = 3.1415926
    
    movies = {"chengnian_movies": ["日韩", "欧美", "国产"], "qingshaonian_movies": ["黑猫警长", "熊出没", "大头儿子"]}
    
    return templates.TemplateResponse(
        "index.html", # 模板文件
        {   
            "request": request,
            "user": name,
            "age": age,
            "books": books,
            "info": info,
            "pai": pai,
            "movies": movies
        }, # context上下文对象，一个字典
    )


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)