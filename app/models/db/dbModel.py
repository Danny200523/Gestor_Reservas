from sqlmodel import SQLModel, Field
from typing import Optional
from enum import Enum
from pydantic import BaseModel, EmailStr, constr, validator

class EstadoReserva(str, Enum):
    pendiente = "pendiente"
    aceptada = "aceptada"
    rechazada = "rechazada"

class Roles(int, Enum):
    admin = 1
    usuario = 0

class Usuarios(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    email: str
    contrasena: str
    rol: int = Field(default=Roles.usuario.value)

class Salas(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    sede: str
    capacidad: int
    recursos: str

class Reservas(SQLModel, table=True):
    id: Optional[int] = Field(default=None,primary_key=True)
    id_sala: int = Field(foreign_key="salas.id")
    id_usuario: int = Field(foreign_key="users.id")
    fecha: str
    hora_inicio: str
    hora_fin: str
    estado: EstadoReserva = Field(default=EstadoReserva.pendiente)

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
