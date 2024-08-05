import sys
from db import execute_sql

def main():
    while True:
        print("\nOpciones: a) Agregar receta, c) Actualizar receta, d) Eliminar receta, e) Listado de recetas, f) Buscar recetas, g) Salir")
        option = input("Seleccione una opción: ").lower()
        
        if option == 'a':
            agregar_receta()
        elif option == 'c':
            actualizar_receta()
        elif option == 'd':
            eliminar_receta()
        elif option == 'e':
            listar_recetas()
        elif option == 'f':
            buscar_recetas()
        elif option == 'g':
            print("Saliendo del programa...")
            sys.exit()
        else:
            print("Opción no válida. Intente de nuevo.")

def agregar_receta():
    # Implementar lógica para agregar receta
    pass

# Implementar las demás funciones aquí...

if __name__ == "__main__":
    main()
