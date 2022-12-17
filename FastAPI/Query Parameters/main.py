from fastapi import FastAPI

app = FastAPI()


db = [
    {"item_id": "1"},
    {"item_id": "2"},
    {"item_id": "3"},
    {"item_id": "4"},
]


@app.get("/items/")
async def get_item(skip: int = 0, limit: int = 10):
    return db[skip: skip + limit]


@app.get("/user/{user_id}")
async def get_user(user_id: int, user: str | None = None):
    if user:
        return {"user": user, "user_id": user_id}
    return {"user_id": user_id}


@app.get("/user/{user_id}/item/{item_id}")
async def read_user_item(user_id: int, item_id: int, long: bool = False):
    item = {"owner_id": user_id, "item_id": item_id}
    if long:
        item.update({"description": "This item has long description"})
    return item
