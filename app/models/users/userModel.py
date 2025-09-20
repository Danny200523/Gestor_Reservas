from fastapi import Depends
from sqlmodel import Session
from app.models.db.dbModel import Usuarios, Roles, Reservas
from app.auth.jwt import create_access_token
from app.utils.security import hash_password
from app.db.db import get_session
from app.auth.service import LoginIn, TokenOut
from fastapi import HTTPException
from sqlmodel import select
from datetime import datetime

def createUser(db: Session, body):
    if not body:
        raise HTTPException(status_code=400, detail="Data incompleta")
    hashed_pass = hash_password(body.password)
    newUser = Usuarios(
        nombre=body.nombre,
        email=body.email,
        contrasena=hashed_pass,
        rol=body.rol if body.rol is not None else 0
    )
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

def deleteUser(db: Session, id):
    if not id:
        raise HTTPException(status_code=400, detail="Data incompleta")
    statement = select(Usuarios).where(Usuarios.id == id)
    user = db.exec(statement).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(user)
    db.commit()
    return {"message": "Usuario eliminado exitosamente"}

def updateUser(db:Session, body, id):
    if not body:
        raise HTTPException(status_code=400, detail="Data incompleta")
    statement = select(Usuarios).where(Usuarios.id == id)
    user = db.exec(statement).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    user.nombre = body.nombre
    user.email = body.email
    user.contrasena = hash_password(body.contrasena)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login(body: LoginIn, session: Session) -> TokenOut:
    if not body:
        raise HTTPException(status_code=400, detail="Data incompleta")
    user = session.exec(select(Usuarios).where(Usuarios.email == body.email)).first()
    if not user:
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    from app.utils.security import verify_password
    if not verify_password(body.password, user.contrasena):
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    token = create_access_token({"email": user.email, "uid": user.id, "rol": user.rol})
    return TokenOut(access_token=token, token_type="bearer")
