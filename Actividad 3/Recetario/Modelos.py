from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Receta(Base):
    __tablename__ = 'recetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)

    ingredientes = relationship("Ingrediente", back_populates="receta")
    pasos = relationship("Paso", back_populates="receta")

class Ingrediente(Base):
    __tablename__ = 'ingredientes'
    id = Column(Integer, primary_key=True)
    receta_id = Column(Integer, ForeignKey('recetas.id'))
    nombre = Column(String(100), nullable=False)
    cantidad = Column(String(100), nullable=False)

    receta = relationship("Receta", back_populates="ingredientes")

class Paso(Base):
    __tablename__ = 'pasos'
    id = Column(Integer, primary_key=True)
    receta_id = Column(Integer, ForeignKey('recetas.id'))
    descripcion = Column(Text, nullable=False)
    orden = Column(Integer)

    receta = relationship("Receta", back_populates="pasos")
