from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship("Usuario", back_populates="posts")

Usuario.posts = relationship("Post", order_by=Post.id, back_populates="usuario")
