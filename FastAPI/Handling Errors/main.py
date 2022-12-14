from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(req: Request, exc: UnicornException):
    return JSONResponse(
        status_code = status.HTTP_418_IM_A_TEAPOT,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow...",},
    )


items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def get_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"})
    return items[item_id]


@app.get("/unicorns/{name}")
async def get_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}