import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__= "usuario"
    id = Column(Integer, primary_key = True)
    favorito = relationship("Favorito", back_populates="usuario")
    email = Column(String(50), nullable = False, unique = True)
    password = Column(String(20), nullable = False)
    fecha_sub = Column(Date, nullable = False)
    nombre = Column(String(50), nullable = False)
    apellido = Column(String(50), nullable = True)

class Favorito(Base):
    __tablename__= "favorito"
    id = Column(Integer, primary_key = True)

    usuario = relationship("Usuario", back_populates="favorito")
    usuario_id = Column(Integer, ForeignKey("usuario.id"))

    planeta = relationship("planeta")
    planeta_id = Column(Integer, ForeignKey("planeta.id"))

    personaje = relationship("personaje")
    personaje_id = Column(Integer, ForeignKey("personaje.id"))

    vehiculo = relationship("vehiculo")
    vehiculo_id = Column(Integer, ForeignKey("vehiculo.id"))

    pelicula = relationship("pelicula")
    pelicula_id = Column(Integer, ForeignKey("pelicula.id"))
    

class Planeta(Base):
    __tablename__= "planeta"
    id = Column(Integer, primary_key = True)
    name = Column(String(20))
    population = Column(Integer)
    climate = Column(String(20))
    terrain = Column(String(20))
    gravity = Column(String(20))

class Personaje(Base):
    __tablename__= "personaje"
    id = Column(Integer, primary_key = True)
    name = Column(String(20))
    hair_color = Column(String(20))
    eyes_color = Column(String(20))
    gender = Column(String(20))
    brithday = Column(Date)

class Vehiculo(Base):
    __tablename__= "vehiculo"
    id = Column(Integer, primary_key = True)
    name = Column(String(20))
    model = Column(String(20))
    max_speed = Column(Float)

class Pelicula(Base):
    __tablename__= "pelicula"
    id = Column(Integer, primary_key = True)
    title = Column(String(20))
    lenght = Column(Integer)
    cast = Column(String)
 

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')