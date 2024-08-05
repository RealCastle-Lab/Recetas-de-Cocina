from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Añadir un nuevo usuario
nuevo_usuario = Usuario(nombre='Juan Perez')
session.add(nuevo_usuario)
session.commit()

# Consultar todos los usuarios
usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(usuario.nombre)
