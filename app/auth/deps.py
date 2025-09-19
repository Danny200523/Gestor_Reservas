from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select
from app.db.db import get_session
from app.models.db.dbModel import Usuarios
from app.auth.jwt import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login", auto_error=True)

def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session)
) -> Usuarios:
    payload = verify_token(token)
    email = payload.get("email") if payload else None
    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

    user = session.exec(select(Usuarios).where(Usuarios.email == email)).first()
    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    return user
