import json
import os

ARCHIVO_AUTORES = "autores.json"
ARCHIVO_LIBROS = "libros.json"

# Funciones 
def cargar_datos(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w") as f:
            json.dump([], f)
        return []
    try:
        with open(nombre_archivo, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"⚠️ Error al leer {nombre_archivo}. Se reiniciará vacío.")
        return []

def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

# Gestión de Autores
def agregar_autor():
    nombre = input("Ingrese el nombre del autor: ").strip()
    nacionalidad = input("Ingrese la nacionalidad del autor: ").strip()

    if not nombre or not nacionalidad:
        print("❌ Los campos no pueden estar vacíos.\n")
        return

    autores = cargar_datos(ARCHIVO_AUTORES)
    for autor in autores:
        if autor["nombre"].lower() == nombre.lower():
            print("⚠️ Este autor ya existe.\n")
            return

    autores.append({"nombre": nombre, "nacionalidad": nacionalidad})
    guardar_datos(ARCHIVO_AUTORES, autores)
    print("✅ Autor agregado exitosamente.\n")

# Gestión de Libros
def agregar_libro():
    titulo = input("Ingrese el título del libro: ").strip()
    genero = input("Ingrese el género: ").strip()
    anio = input("Ingrese el año de publicación: ").strip()
    autor = input("Ingrese el nombre del autor: ").strip()

    if not titulo or not genero or not anio or not autor:
        print("❌ Todos los campos son obligatorios.\n")
        return

    if not anio.isdigit():
        print("❌ El año debe ser un número.\n")
        return

    libros = cargar_datos(ARCHIVO_LIBROS)
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower() and libro["autor"].lower() == autor.lower():
            print("⚠️ Este libro ya existe en el sistema.\n")
            return

    libros.append({
        "titulo": titulo,
        "genero": genero,
        "anio": int(anio),
        "autor": autor
    })
    guardar_datos(ARCHIVO_LIBROS, libros)
    print("✅ Libro agregado exitosamente.\n")

# Mostrar y Buscar
def mostrar_informacion():
    print("\n📚 LIBROS:")
    libros = cargar_datos(ARCHIVO_LIBROS)
    if libros:
        for libro in libros:
            print(f"- {libro['titulo']} ({libro['anio']}) | {libro['genero']} | Autor: {libro['autor']}")
    else:
        print("No hay libros registrados.")

    print("\n🖋️ AUTORES:")
    autores = cargar_datos(ARCHIVO_AUTORES)
    if autores:
        for autor in autores:
            print(f"- {autor['nombre']} ({autor['nacionalidad']})")
    else:
        print("No hay autores registrados.")
    print()

def buscar_libro():
    criterio = input("Ingrese título o autor a buscar (Enter para cancelar): ").strip().lower()
    if not criterio:
        print("🔙 Búsqueda cancelada.\n")
        return

    libros = cargar_datos(ARCHIVO_LIBROS)
    resultados = [libro for libro in libros if
                  criterio in libro["titulo"].lower() or
                  criterio in libro["autor"].lower()]

    if resultados:
        print("\n📚 Resultados encontrados:")
        for libro in resultados:
            print(f"- {libro['titulo']} ({libro['anio']}) | {libro['genero']} | Autor: {libro['autor']}")
    else:
        print("⚠️ No se encontraron resultados.\n")

# Menú Principal
def menu():
    while True:
        print("📘 SISTEMA DE GESTIÓN DE LIBROS Y AUTORES")
        print("1. Agregar autor")
        print("2. Agregar libro")
        print("3. Mostrar información")
        print("4. Buscar libro")
        print("5. Salir")
        opcion = input("Seleccione una opción: ").strip()
        print()

        if opcion == "1":
            agregar_autor()
        elif opcion == "2":
            agregar_libro()
        elif opcion == "3":
            mostrar_informacion()
        elif opcion == "4":
            buscar_libro()
        elif opcion == "5":
            print("Saliendo del programa... 👋")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.\n")

# Ejecutar programa
if __name__ == "__main__":
    menu()
