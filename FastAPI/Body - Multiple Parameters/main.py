from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    name: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(title="Id of an item", ge=0, le=1000),
    q: str | None = Query(default=None, description="Query param"),
    item: Item | None = None,
    user: User | None = None,  # using to models
    importance: int = Body(ge=0)  # otherwise will be count as query parameter
):
    result = {"item_id": item_id}
    if q is not None:
        result.update({"q": q})
    if item is not None:
        result.update({"item": item})
    if user is not None:
        result.update({"user": user})

    return result
