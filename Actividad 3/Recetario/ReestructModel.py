from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['recetario']

# No hay necesidad de definir clases de modelo como en SQLAlchemy
