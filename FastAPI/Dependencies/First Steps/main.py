from fastapi import FastAPI, Depends

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get('/items/')
async def get_items(commons: dict = Depends(common_parameters)):
    return commons

@app.get('/users/')
async def get_users(commons: dict = Depends(common_parameters)):
    return commons