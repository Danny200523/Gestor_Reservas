from fastapi import APIRouter, Depends
from app.models.reservas.reservaModel import newRes, deleteRes, getReservasByUsuario, getAll, acceptRes, rejectRes
from app.models.db.dbModel import Usuarios, Reservas
from sqlmodel import Session
from app.db.db import get_session
from app.auth.service import LoginIn, TokenOut
from pydantic import BaseModel, EmailStr, constr, validator
from app.utils.adminProperties import admin_required

router = APIRouter()

@router.post('/new-reserva')
def res(res : Reservas,session: Session = Depends(get_session)):
    # Crea una nueva reserva en el sistema
    return newRes(session, res)

@router.delete('/delete-res', dependencies=[Depends(admin_required)])
def delRes(id: int, session: Session = Depends(get_session)):
    return deleteRes(session, id)

@router.get('/reservasByUsuario/{id_usuario')
def getResById(id_usuario: int, session: Session = Depends(get_session)):
    return getReservasByUsuario(session, id_usuario)

@router.get('/reservas-all', dependencies=[Depends(admin_required)])
def get_all(session: Session = Depends(get_session)):
    return getAll(session)

@router.put('/accept-res/{id}')
def aceptarReservas(id:int,session:Session = Depends(get_session)):
    return acceptRes(session,id)

@router.put('/reject-res/{id}')
def rechazarReservas(id:int,session:Session = Depends(get_session)):
    return rejectRes(session,id)
