from fastapi import FastAPI
from fastapi import Query

app = FastAPI()


@app.get('/items/')
async def read_items(q: str | None = Query(default=None, min_length=3, max_length=50, regex="^a")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get('/lists/')
async def get_lists(q: list[str] | None = Query(default=None,
                                                title="Query Params",
                                                description="Query string for the items",
                                                alias="item-query",
                                                deprecated=True),
                    hidden: str | None = Query(default=None, include_in_schema=False)):
    result = {"q": q}
    if hidden is not None:
        result.update({"hidden": hidden})
    return result
