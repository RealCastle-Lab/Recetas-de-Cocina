session = Session()

# Para agregar una receta
nueva_receta = Receta(nombre='Paella', descripcion='Deliciosa paella española')
session.add(nueva_receta)
session.commit()

# Para consultar recetas
recetas = session.query(Receta).all()
for receta in recetas:
    print(receta.nombre)
