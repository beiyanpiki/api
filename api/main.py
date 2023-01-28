from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import bili
from api.utils import response as resp

app = FastAPI()

# CORS Support
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://mki.moe", "https://mik.moe"],
    allow_origin_regex=['https://.*\.mki\.moe', "https://.*\.mik\.moe"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Bilibili Api
app.include_router(bili.router)


@app.get("/ping")
async def ping():
    return resp.common_resp(data='Pong!')
