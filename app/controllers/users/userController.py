from app.models.db.dbModel import Users
from fastapi import Depends
from sqlmodel import Session
import bcrypt
from app.db.db import get_session
from app.models.users.userModel import createUser

def register(body,session:Session = Depends(get_session)):
    if body:
        return print("Data Incompleta")
    createUser(session,body)