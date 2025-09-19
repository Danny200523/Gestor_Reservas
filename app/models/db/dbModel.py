from sqlmodel import SQLModel, Field
from typing import Optional
from enum import Enum

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