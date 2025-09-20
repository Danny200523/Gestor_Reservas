"""
Rutas API para gestión de usuarios y reservas.
Incluye registro, login, CRUD de usuarios y creación de reservas.
Algunas rutas requieren permisos de administrador.
"""

from fastapi import APIRouter, Depends
from app.models.users.userModel import createUser, login, deleteUser, updateUser
from app.models.db.dbModel import Usuarios, Reservas
from sqlmodel import Session
from app.db.db import get_session
from app.auth.service import LoginIn, TokenOut
from pydantic import BaseModel, EmailStr, constr, validator
from app.utils.adminProperties import admin_required
from app.models.db.dbModel import UserCreate


# Router para rutas de usuarios
# Configurar prefix="/users" y tags=["users"] si se necesita
router = APIRouter()

@router.post('/register', summary="Register", description="Genera el registro de usuarios o admin nuevos", response_model=Usuarios)
def register_user(user: UserCreate, session: Session = Depends(get_session)):
    # Registra un nuevo usuario en el sistema
    return createUser(session, user)

@router.post('/login', summary="Login", description="Crea sesion para poder gestionar la base de datos", response_model=TokenOut)
def login_user(body: LoginIn, session: Session = Depends(get_session)):
    # Autentica usuario y devuelve token JWT
    return login(body, session)

@router.delete('/delete-user/{id}', dependencies=[Depends(admin_required)])
def delete(id : int, session: Session = Depends(get_session)):
    # Elimina un usuario (solo admin)
    return deleteUser(session, id)

@router.put('/update-user/{id}', dependencies=[Depends(admin_required)])
def update(id : int, user: Usuarios, session: Session = Depends(get_session)):
    # Actualiza datos de un usuario (solo admin)
    return updateUser(session, user, id)

@router.get('/todo', dependencies=[Depends(admin_required)])
def get_all(session: Session = Depends(get_session)):
    # Obtiene todos los usuarios (solo admin)
    return session.query(Usuarios).all()


