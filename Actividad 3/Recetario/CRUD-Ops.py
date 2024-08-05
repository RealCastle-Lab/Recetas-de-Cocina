# Agregar una receta
db.recetas.insert_one(receta)

# Actualizar una receta
db.recetas.update_one({"nombre": "Paella"}, {"$set": {"descripcion": "Paella valenciana"}})

# Eliminar una receta
db.recetas.delete_one({"nombre": "Paella"})

# Listar todas las recetas
for receta in db.recetas.find():
    print(receta)

# Buscar una receta por nombre
resultado = db.recetas.find_one({"nombre": "Paella"})
print(resultado)
