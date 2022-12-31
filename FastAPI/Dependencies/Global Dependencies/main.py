from fastapi import FastAPI, Depends, Header, HTTPException





async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key

app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)], tags=["Items"])

@app.get("/items", )
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]

@app.get("/users", )
async def read_items():
    return [{"username": "Rick"}, {"username": "Morty"}]
