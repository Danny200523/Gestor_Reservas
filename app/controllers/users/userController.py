from app.models.db.dbModel import Usuarios
from fastapi import Depends
from sqlmodel import Session
import bcrypt
from app.db.db import get_session
from app.models.users.userModel import createUser

def register(body: Usuarios,session: Session):
    if not body:
        raise print("Data Incompleta")
    return createUser(session,body)