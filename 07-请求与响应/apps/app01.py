from fastapi import APIRouter

app01 = APIRouter()


@app01.get("/user/{id}")
def get_user(id):
    print("id", id)
    return {
        "user_id": id
    }
    
    
@app01.get("/articles/{id}")
def get_user(id:int):
    print("id", id)
    return {
        "articles": id
    }