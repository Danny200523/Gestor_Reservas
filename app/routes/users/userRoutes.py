from fastapi import APIRouter, Depends
from app.models.users.userModel import createUser, login, deleteUser
from app.models.db.dbModel import Usuarios
from sqlmodel import Session
from app.db.db import get_session
from app.auth.service import LoginIn, TokenOut
from pydantic import BaseModel, EmailStr, constr, validator
from app.utils.adminProperties import admin_required
from app.models.db.dbModel import UserCreate


router = APIRouter()

@router.post('/register', summary="Register", description="Genera el registro de usuarios o admin nuevos", response_model=Usuarios)
def register_user(user: UserCreate, session: Session = Depends(get_session)):
    return createUser(session, user)

@router.post('/login', summary="Login", description="Crea sesion para poder gestionar la base de datos", response_model=TokenOut)
def login_user(body: LoginIn, session: Session = Depends(get_session)):
    return login(body, session)

@router.delete('/delete/{id}', dependencies=[Depends(admin_required)])
def delete(id : int, session: Session = Depends(get_session)):
    return deleteUser(session, id)