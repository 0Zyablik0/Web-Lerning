from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get('/items/{item_id}',
         response_model=Item,
         status_code=status.HTTP_200_OK,
         tags=['items', 'get'],
         description="Returns an item by item id"
         )
async def get_file(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_418_IM_A_TEAPOT, detail="Item not found")
    return items[item_id]


@app.put('/items/{item_id}/',
         status_code=status.HTTP_201_CREATED,
         description="Updates Item",
         response_model=Item,
         tags=["items", 'update'])
async def update_item(item_id: str, item: Item):
    item_encoded = jsonable_encoder(item)
    items[item_id] = item_encoded
    return items[item_id]


@app.patch("/items/{item_id}", 
           response_model=Item,
           status_code=status.HTTP_200_OK,
           tags=["items", "patch"],
           description="Patch Item")
async def patch_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item