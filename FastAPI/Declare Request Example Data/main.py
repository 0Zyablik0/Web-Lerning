from fastapi import FastAPI, Body
from pydantic import BaseModel, Field


app = FastAPI()


class Item(BaseModel):
    name: str = Field(example="Foo")
    description: str | None = Field(default=None, example="A very nice Item")
    price: float = Field(example=35.4)
    tax: float | None = Field(default=None, example=3.2)

    class Config:
        schema_extra = {
            "example": {
                "name": "Name",
                "description": "description",
                "price": 1.2,
                "tax": 0.1,
            }
        }


@app.put("/items/{item_id}")
async def update_item(
        item_id: int,
        item: Item = Body(
            examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        )):
    result = {"item_id": item_id, "item": Item}
    return result
