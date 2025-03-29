from pydantic import EmailStr
from sqlmodel import SQLModel, Field
from typing import Optional


class UsuariosResponse(SQLModel):
    id: Optional[int]
    nombre: str
    email: EmailStr
    edad: int


# Esquema para la creación de usuarios (sin el campo id)
class UsuariosCreate(SQLModel):
    nombre: str
    email: EmailStr
    edad: int

# Esquema para la respuesta de usuarios (incluye el campo id)
class Usuarios(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Clave primaria autoincremental
    nombre: str
    email: EmailStr
    edad: int