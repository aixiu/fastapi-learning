# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2024/04/22 15:35:53

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/items", tags=["这是items测试接口"], 
          summary="this is items测试 summary",
          description="this is items测试 description...",
          response_description="items测试 response_description...",
          deprecated=False)
def post_test():
    return {"method": "items数据"}

if __name__ == '__main__':
    uvicorn.run("05-路径操作装饰器方法的参数:app", port=8000, reload=True)