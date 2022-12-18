from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if (item.tax):
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}/")
async def create_item(item_id: int, item: Item, info: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if (info):
        result.update({'info': info})
    return result
