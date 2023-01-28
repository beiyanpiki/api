
from bilibili_api import user
from fastapi import APIRouter, Depends

from api.dependencies import get_token_header
from api.utils import response as resp

router = APIRouter(
    prefix="/api/bili",
    tags=["bilibili"],
    dependencies=[Depends(get_token_header)],
)


@router.get("/check_stream")
async def check_stream(uid: int):
    u = user.User(uid)
    info = await u.get_live_info()
    data = {
        'status': info['live_room']['liveStatus'],
        'roomid': info['live_room']['roomid'],
    }
    return resp.common_resp(data=data)

