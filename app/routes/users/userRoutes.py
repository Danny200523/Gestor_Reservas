from fastapi import APIRouter, Depends
from app.controllers.users.userController import register
from app.models.db.dbModel import Users
from sqlmodel import Session
from app.db.db import get_session



rout = APIRouter()
rout.post('/register')
def register(user: Users,session: Session = Depends(get_session)):
    register(user,session)