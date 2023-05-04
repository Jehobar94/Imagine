from app.db.database import Base
from sqlalchemy import Column,Integer,String,Boolean,DateTime
from datetime import datetime


class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,autoincrement=True)
    nombre = Column(String)
    apellido = Column(String)
    direccion = Column(String)
    Telefono = Column(Integer)
    correo = Column(String)
    creacion = Column(Datetime,default=datetime.now,onupdate=datetime.now)
    estado = Column(Boolean)