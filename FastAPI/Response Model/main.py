from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] | None = None


class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: str
    full_name: str | None = None
    
class UserOut(BaseModel):
    name: str
    email: EmailStr
    full_name: str | None = None


app = FastAPI()


@app.post("/items/", response_model=Item, response_model_exclude_unset=True)
async def create_item(item: Item):
    return item


@app.post("/users/", response_model=UserOut)
async def create_user(user: UserIn):
    return user