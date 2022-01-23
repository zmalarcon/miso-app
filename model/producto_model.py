from sqlalchemy.sql import func
from utils.crypto import uuid4Str
from sqlalchemy import Column, Text, String, DateTime, Float
from .base import Base
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

# Modelo para la entidad Producto
class Producto(Base):
    __tablename__ = "producto"

    id = Column(String(40), primary_key=True, default=uuid4Str)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=False)
    imagen = Column(String(256), nullable=False)
    ranking = Column(Float(32), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

pydantic_parser = sqlalchemy_to_pydantic(Producto)

def producto_convertir_arreglo(arreglo):
    return list(map(producto_convertir, arreglo))

def producto_convertir(fila):
    return pydantic_parser.from_orm(fila).dict()
    