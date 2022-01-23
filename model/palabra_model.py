from utils.crypto import uuid4Str
from sqlalchemy import Column, String, Float
from .base import Base
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

# Modelo para la entidad Producto
class Palabra(Base):
    __tablename__ = "palabra"

    palabra = Column(String(100), primary_key=True, nullable=False)
    ranking = Column(Float(32), nullable=False)

palabra_parser = sqlalchemy_to_pydantic(Palabra)