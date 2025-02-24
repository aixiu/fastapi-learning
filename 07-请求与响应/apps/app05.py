from pathlib import Path

from fastapi import APIRouter, File, UploadFile

app05 = APIRouter()

@app05.post("/file")
async def get_file(file:bytes=File()):
    # 适合小文件上传
    print("file ", file)
    return {
        "file": len(file)
    }
    
@app05.post("/files")
async def get_files(files:list[bytes]=File()):
    # 适合小文件上传
    # print("file ", files)
    for file in files:
        print(len(file))
    return {
        "file": len(files)
    }

# 常用的上传单个文件方法    
@app05.post("/uploadFile")
async def uploadFile(file: UploadFile):
    # 适合大文件上传
    print("file ", file)
    
    file_path = Path("image")
    
    if not file_path.exists():
        file_path.mkdir()
    # 文件保存  
    with open(file=f"{file_path}/{file.filename}", mode="wb") as f:
        for line in file.file:
            f.write(line)
    
    return {
        "file": file.filename
    }

# 常用的上传多个文件方法    
@app05.post("/uploadFiles")
async def UploadFiles(files:list[UploadFile]):
    # 适合大文件上传
    print("file ", files)
    
    return {
        "names": [file.filename for file in files]
    }