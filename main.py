from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app="main:app", port=8000, reload=True)
