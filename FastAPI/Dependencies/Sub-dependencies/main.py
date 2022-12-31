from fastapi import FastAPI, Depends, Cookie, Query, status


app = FastAPI()


async def query_extractor(q: str | None = Query(default=None)):
    return q


async def query_or_cookie_extractor(q: str = Depends(query_extractor), last_query: str | None = Cookie(default=None)):
    print(q, last_query)
    if not q:
        return last_query

    return q


@app.get("/items/", status_code=status.HTTP_200_OK, tags=['Items'])
async def read_items(query_or_cookie: str = Depends(query_or_cookie_extractor)):
    return {
        "query_or_cookie": query_or_cookie,
    }
