from sqlmodel import SQLModel, Field

class Users(SQLModel, table=True):
    id: [int] = Field(default=None, primary_key=True)
    nombre: str
    email: str
    contrasena: str
    rol: bool

class Salas(SQLModel, table=True):
    id: [int] = Field(default=None, primary_key=True)
    nombre: str
    sede: str
    capacidad: int
    recursos: str

class Reservas(SQLModel, table=True):
    id: [int] = Field(default=None,primary_key=True, foreign_key="salas.id", foreign_key="users.id")
    id_sala: int
    id_usuario: int
    fecha: str
    hora_inicio: str
    hora_fin: str
    estado: {"pendiente", "aceptada", "rechazada"}