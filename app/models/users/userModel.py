import bcrypt
from sqlmodel import Session
from app.models.db.dbModel import Users


async def createUser(db:Session,body):
    salt = bcrypt.gensalt(rounds=12)
    hasedpass = bcrypt.hashpw(newUser.password.encode('utf-8'), salt)
    newUser = Users(username = body['nombre'],email = body['email'],password = body['contrasena'])
    Session.add(newUser)
    Session.commit()
    Session.refresh(newUser)