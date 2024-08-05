CREATE TABLE IF NOT EXISTS recetas (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    descripcion TEXT
);

CREATE TABLE IF NOT EXISTS ingredientes (
    id INTEGER PRIMARY KEY,
    receta_id INTEGER,
    nombre TEXT NOT NULL,
    cantidad TEXT NOT NULL,
    FOREIGN KEY (receta_id) REFERENCES recetas (id)
);

CREATE TABLE IF NOT EXISTS pasos (
    id INTEGER PRIMARY KEY,
    receta_id INTEGER,
    paso TEXT NOT NULL,
    orden INTEGER,
    FOREIGN KEY (receta_id) REFERENCES recetas (id)
);
