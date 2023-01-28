import os
from fastapi import Header, HTTPException


async def get_token_header(token: str = Header()):
    admin_token = os.getenv('ADMIN_TOKEN', 'admin_token_here')
    if token != admin_token:
        raise HTTPException(status_code=400, detail="Token header invalid")
