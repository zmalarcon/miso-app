import bcrypt
from sqlalchemy.sql import func
from sqlalchemy import Column, Text, String, DateTime
from .base import Base
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from utils.crypto import uuid4Str
# Modelo para la base de datos
class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(String(40), primary_key=True, default=uuid4Str)
    username = Column(String(30), nullable=False, unique=True)
    email = Column(String(60), nullable=False, unique=True)
    phone = Column(String(60), nullable=False)
    password = Column(Text)
    salt = Column(Text)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    
    def verify_password(self, password):
        pwhash = bcrypt.hashpw(password.encode('utf8'), self.salt.encode('utf8')).decode("utf-8")
        return self.password == pwhash



pydantic_parser = sqlalchemy_to_pydantic(Usuario)