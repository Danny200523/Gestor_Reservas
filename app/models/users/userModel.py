from fastapi import Depends
from sqlmodel import Session
from app.models.db.dbModel import Usuarios, Roles
from app.auth.jwt import create_access_token
from app.utils.security import hash_password
from app.db.db import get_session
from app.auth.service import LoginIn, TokenOut
from fastapi import HTTPException
from sqlmodel import select

def createUser(db: Session, body):
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

def login(body: LoginIn, session: Session) -> TokenOut:
    user = session.exec(select(Usuarios).where(Usuarios.email == body.email)).first()
    if not user:
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    from app.utils.security import verify_password
    if not verify_password(body.password, user.contrasena):
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    token = create_access_token({"email": user.email, "uid": user.id, "rol": user.rol})
    return TokenOut(access_token=token, token_type="bearer")
