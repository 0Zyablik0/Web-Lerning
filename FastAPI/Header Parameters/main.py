from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(
        user_agent: list[str] | None = Header(default=None),
        x_token: list[str] | None = Header(default=None)):
    return {"User-Agent": user_agent,
            "X-Token": x_token}
