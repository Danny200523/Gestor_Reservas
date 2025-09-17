from app.models.db.dbModel import Users
from sqlmodel import Session
import bcrypt
from app.models.users.userModel import createUser

def register(session:Session = Depends(get_session), body:dict):
    body = request.json()
    createUser(session,body)