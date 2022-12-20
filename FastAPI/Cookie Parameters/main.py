from fastapi import FastAPI, Cookie


app = FastAPI()


@app.get("/items/")
async def get_items(ads_id: str | None = Cookie(default=None)):
    return {
        "ads_id": ads_id,
    }
