from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Union


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str
    type: str


class BaseItem(BaseModel):
    description: str


class CarItem(BaseModel):
    type = "car"


class PlaneItem(BaseModel):
    type = "plane"
    size: int


app = FastAPI()


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    user_saved = fake_save_user(user)
    return user_saved

items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


@app.get("/items/{item_id}", response_model=Union[CarItem, PlaneItem])
async def read_item(item_id: int):
    return items[item_id]