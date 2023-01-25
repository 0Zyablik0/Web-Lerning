from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.routing import Mount

app = FastAPI()

app.mount("/static", StaticFiles(directory='static'), name='static')