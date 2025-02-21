from fastapi import APIRouter, Form

app04 = APIRouter()


@app04.post("/regin")
async def reg(username: str = Form(), password: str = Form()):
    print(f"username: {username}, password: {password}")
    # 注册，实现用户名和密码的数据库添加
    return {"username": username, "password": password}
