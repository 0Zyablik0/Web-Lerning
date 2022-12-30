from fastapi import FastAPI, Depends, Query, status

app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]
fake_users_db = [{"user_name": "john_wick"}, {
    "user_name": "will_smith"}, {"user_name": "joe"}]


class CommonParameters:
    def __init__(self, q: str | None = Query(default=None), skip: int = Query(default=0), limit: int = Query(default=100)):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/", status_code=status.HTTP_200_OK, tags=['Items', "Read"])
async def read_items(commons: CommonParameters = Depends(CommonParameters)):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response


@app.get("/users/", status_code=status.HTTP_200_OK, tags=['Users', "Read"])
async def read_users(commons: CommonParameters = Depends()):  # shortcut for Depends
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    users = fake_users_db[commons.skip: commons.skip + commons.limit]
    response.update({"users": users})
    return response
