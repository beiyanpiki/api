from fastapi import FastAPI

from api.routers import bili
from api.utils import response as resp

app = FastAPI()

app.include_router(bili.router)


@app.get("/ping")
async def ping():
    return resp.common_resp(data='Pong!')
