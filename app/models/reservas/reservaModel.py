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
from app.models.db.dbModel import EstadoReserva

def getAll(db:Session):
    statement = select(Reservas)
    reservas = db.exec(statement).all()
    if not reservas:
        raise HTTPException(status_code=404, detail="No se encontraron reservas")
    return reservas

def newRes(db:Session, body):
    if not body:
        raise HTTPException(status_code=400, detail="Data incompleta")
    try:
        hour_inicio = datetime.strptime(body.hora_inicio, "%H:%M:%S")
        hour_fin = datetime.strptime(body.hora_fin, "%H:%M:%S")
        duration = int((hour_fin - hour_inicio).total_seconds() / 60)
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de hora incorrecto, use HH:MM:SS")

    if duration != 60:
        raise HTTPException(status_code=400, detail="La reserva debe durar 60 minutos")
    data = getAll(db)
    for i in range(len(data)):
        if data[i].fecha == body.fecha and data[i].hora_inicio == body.hora_inicio and data[i].hora_fin == body.hora_fin and data[i].id_sala == body.id_sala:
            raise HTTPException(status_code=400, detail="Ya existe una reserva para esta fecha")
    newRes = Reservas(
        id_sala=body.id_sala,
        id_usuario=body.id_usuario,
        fecha=body.fecha,
        hora_inicio=body.hora_inicio,
        hora_fin=body.hora_fin,
        estado=body.estado
    )
    db.add(newRes)
    db.commit()
    db.refresh(newRes)
    return newRes

def deleteRes(db:Session, id:int):
    if not id:
        raise HTTPException(status_code=400, detail="Data incompleta")
    res = select(Reservas).where(Reservas.id == id)
    res = db.exec(res).first()
    if not res:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    db.delete(res)
    db.commit()
    return {"message": "Reserva eliminada exitosamente"}

def getReservasByUsuario(db:Session, id:int):
    statement = select(Reservas).where(Reservas.id_usuario == id)
    reservas = db.exec(statement).all()
    if not reservas:
        raise HTTPException(status_code=404, detail="No se encontraron reservas para este usuario")
    return reservas

def acceptRes(session:Session, id):
    if not id:
        raise HTTPException(status_code=400, detail="Data incompleta")
    statement = select(Reservas).where(Reservas.id == id)
    res = session.exec(statement).first()
    if not res:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    res.estado = EstadoReserva.Confirmado
    session.add(res)
    session.commit()
    session.refresh(res)
    return res

def rejectRes(session:Session, id):
    if not id:
        raise HTTPException(status_code=400, detail="Data incompleta")
    statement = select(Reservas).where(Reservas.id == id)
    res = session.exec(statement).first()
    if not res:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    res.estado = EstadoReserva.Rechazado
    session.add(res)
    session.commit()
    session.refresh(res)
    return res