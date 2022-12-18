from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get('/items/{item_id}')
async def get_item(
    item_id: int = Path(default= ..., title="The ID of the item to get", gt=0, le=1000),
    q: str | None = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
