from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from app.db.db import get_session
from app.models.db.dbModel import Usuarios
from app.auth.service import TokenOut
from app.auth.jwt import create_access_token
from app.auth.deps import get_current_user
from app.utils.security import verify_password

router = APIRouter(prefix="/user")

@router.post("/login", response_model=TokenOut)
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    print(f"Login attempt with username: {form_data.username}, password: {form_data.password}")
    usuario = session.exec(select(Usuarios).where(Usuarios.email == form_data.username.lower())).first()
    if not usuario:
        print(f"Usuario no encontrado para email: {form_data.username.lower()}")
        raise HTTPException(status_code=401, detail="❌Credenciales inválidas.")
    print(f"Usuario encontrado: {usuario.email}")
    print(f"Stored hash for {usuario.email}: {usuario.contrasena}")
    password_check = verify_password(form_data.password, usuario.contrasena)
    print(f"Resultado de verificar_contraseña: {password_check}")
    if not password_check:
        print(f"Contraseña incorrecta para usuario: {usuario.email}")
        raise HTTPException(status_code=401, detail="❌Credenciales inválidas.")

    token = create_access_token({"email": usuario.email, "uid": usuario.id, "rol": usuario.rol})
    return TokenOut(access_token=token, token_type="bearer")

# Ejemplo de endpoint protegido
@router.get("/me")
def me(current_user: Usuarios = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "nombre": current_user.nombre,
        "email": current_user.email,
        "rol": current_user.rol,
    }
