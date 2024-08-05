receta = {
    "nombre": "Paella",
    "descripcion": "Deliciosa paella española",
    "ingredientes": [
        {"nombre": "Arroz", "cantidad": "1 taza"},
        {"nombre": "Pollo", "cantidad": "200 gr"}
    ],
    "pasos": [
        {"paso": "Calentar el aceite en una paellera.", "orden": 1},
        {"paso": "Añadir el arroz y el pollo y sofreír.", "orden": 2}
    ]
}
db.recetas.insert_one(receta)
