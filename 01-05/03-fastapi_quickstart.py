# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2024/04/22 11:02:20

# 需先安装 fastapi，uvicorn 模块
# pip install fastapi
# pip install uvicorn

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def home():
    return {"user_id": "1001"}

@app.get("/shop")
async def shop():
    return {"shop": "商品信息"}

if __name__ == '__main__':
    try:
        uvicorn.run('03-fastapi_quickstart:app', host='127.0.0.1', port=8080, reload=True)
    
    except KeyboardInterrupt:
        print("用户中断了程序")
