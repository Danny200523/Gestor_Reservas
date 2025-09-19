import os
from datetime import timedelta

JWT_SECRET = os.getenv("jwt_secret")
JWT_ALG    = os.getenv("jwt_alg")
JWT_EXPIRE = os.getenv("jwt_expire")   # 1h
