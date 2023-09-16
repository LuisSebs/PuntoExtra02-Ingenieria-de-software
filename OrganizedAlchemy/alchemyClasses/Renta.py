from alchemyClasses import db
from sqlalchemy import Column, Integer, String, Date, Boolean
from hashlib import sha256
from utils.CryptoUtils import cipher
from datetime import datetime

class Renta(db.Model):

    __tablename__ = 'rentar'
    idRenta = Column(Integer, primary_key=True)
    idUsuario = Column(Integer)
    idPelicula = Column(Integer)
    fecha_renta = Column(Date)
    dias_de_renta = Column(Integer)
    estatus = Column(Boolean)

    def __init__(self, idUsuario, idPelicula, dias_de_renta) -> None:
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = datetime.utcnow()
        self.dias_de_renta = dias_de_renta
        self.estatus = 1
    
        