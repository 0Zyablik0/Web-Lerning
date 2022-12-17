from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    lenet = "lenet"
    resnet = "resnet"


app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello world"
    }


# Annotations
@app.get("/items/{item_id}")
async def items(item_id: int):
    return {"id": item_id}


# first match - first use
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# Predefined values
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    match model_name:
        case ModelName.alexnet:
            return {"model_name": model_name, "message": "Deep Learning FTW!"}
        case ModelName.lenet:
            return {"model_name": model_name, "message": "LeCNN all the images"}
        case ModelName.resnet:
            return {"model_name": model_name, "message": "Have some residuals"}
        case _:
            return {"error": "Unknown model"}


# Path
@app.get("/files/{file_path:path}")
async def get_file(file_path: str):
    return {"path": file_path}
