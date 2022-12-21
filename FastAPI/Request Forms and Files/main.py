from fastapi import FastAPI, status, File, UploadFile, Form

app = FastAPI()


@app.post("/files/{file_id}")
async def create_file(
    file_id: int,
    file: bytes = File(),
    fileb: UploadFile = File(),
    token: str = Form()
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
