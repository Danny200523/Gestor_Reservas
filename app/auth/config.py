import os
from datetime import timedelta

JWT_SECRET = os.getenv("JWT_SECRET", "defaultsecret")
JWT_ALG = os.getenv("JWT_ALG", "HS256")
JWT_EXPIRE_STR = os.getenv("JWT_EXPIRE", "1h")  # Default to 1h

def parse_expire(expire_str: str) -> timedelta:
    if expire_str.endswith('h'):
        hours = int(expire_str[:-1])
        return timedelta(hours=hours)
    elif expire_str.endswith('m'):
        minutes = int(expire_str[:-1])
        return timedelta(minutes=minutes)
    else:
        # Assume minutes if no suffix
        return timedelta(minutes=int(expire_str))

JWT_EXPIRE = parse_expire(JWT_EXPIRE_STR)
