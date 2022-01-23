from sqlalchemy.sql import func
from sqlalchemy import Column, String, DateTime, ForeignKey
from .base import Base
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from utils.crypto import uuid4Str

# Modelo para la entidad sesión
class Sesion(Base):
    __tablename__ = "sesion"

    id = Column(String(40), primary_key=True, default=uuid4Str)
    user_id = Column(String(40), ForeignKey('usuario.id'))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

pydantic_parser = sqlalchemy_to_pydantic(Sesion)