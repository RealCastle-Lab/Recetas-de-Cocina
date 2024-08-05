from sqlalchemy import create_engine

# Conectar a una base de datos SQLite en memoria
engine = create_engine('sqlite:///:memory:')

# Si deseas conectar a un archivo de base de datos real, puedes hacerlo así:
# engine = create_engine('sqlite:///mi_base_de_datos.db')
