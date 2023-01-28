from enum import Enum, unique
from typing import Any, TypedDict


@unique
class StatusCode(Enum):
    SUCCESS = 0


class Response(TypedDict):
    code: int
    msg: str
    data: Any

def common_resp(code: int = StatusCode.SUCCESS,
                msg: str = 'Success.',
                data: Any = None) -> Response:
    return {"code": code, 'msg': msg, 'data': data}
