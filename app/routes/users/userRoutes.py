from fastapi import APIRouter, Depends
from app.models.users.userModel import createUser, login
from app.models.db.dbModel import Usuarios
from sqlmodel import Session
from app.db.db import get_session
from app.auth.service import LoginIn, TokenOut
from pydantic import BaseModel, EmailStr, constr, validator

class UserCreate(BaseModel):
    nombre: constr(min_length=1)
    email: EmailStr
    password: constr(min_length=6)
    rol: int = 0

    @validator('rol')
    def role_must_be_valid(cls, v):
        if v not in (0, 1):
            raise ValueError('rol must be 0 or 1')
        return v

router = APIRouter()

@router.post('/register', summary="Register", description="Genera el registro de usuarios o admin nuevos", response_model=Usuarios)
def register_user(user: UserCreate, session: Session = Depends(get_session)):
    return createUser(session, user)

@router.post('/login', summary="Login", description="Crea sesion para poder gestionar la base de datos", response_model=TokenOut)
def login_user(body: LoginIn, session: Session = Depends(get_session)):
    return login(body, session)
