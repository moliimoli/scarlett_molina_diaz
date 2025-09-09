import json
import os

ARCHIVO_AUTORES = "autores.json"
ARCHIVO_LIBROS = "libros.json"

def cargar_datos(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w") as f:
            json.dump([], f)
        return []
    with open(nombre_archivo, "r") as f:
        return json.load(f)

def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w") as f:
        json.dump(datos, f, indent=4)

def agregar_autor():
    nombre = input("Ingrese el nombre del autor: ")
    nacionalidad = input("Ingrese la nacionalidad del autor: ")
    autores = cargar_datos(ARCHIVO_AUTORES)
    autores.append({"nombre": nombre, "nacionalidad": nacionalidad})
    guardar_datos(ARCHIVO_AUTORES, autores)
    print("✅ Autor agregado exitosamente.\n")

def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    genero = input("Ingrese el género: ")
    anio = input("Ingrese el año de publicación: ")
    autor = input("Ingrese el nombre del autor: ")
    libros = cargar_datos(ARCHIVO_LIBROS)

    for libro in libros:
        if libro["titulo"].lower() == titulo.lower() and libro["autor"].lower() == autor.lower():
            print("⚠️ Este libro ya existe en el sistema.\n")
            return

    libros.append({
        "titulo": titulo,
        "genero": genero,
        "anio": anio,
        "autor": autor
    })
    guardar_datos(ARCHIVO_LIBROS, libros)
    print("✅ Libro agregado exitosamente.\n")

def mostrar_informacion():
    print("\n📚 LIBROS:")
    libros = cargar_datos(ARCHIVO_LIBROS)
    for libro in libros:
        print(json.dumps(libro, indent=4, ensure_ascii=False))

    print("\n🖋️ AUTORES:")
    autores = cargar_datos(ARCHIVO_AUTORES)
    for autor in autores:
        print(json.dumps(autor, indent=4, ensure_ascii=False))
    print()

def menu():
    while True:
        print("📘 SISTEMA DE GESTIÓN DE LIBROS Y AUTORES")
        print("1. Agregar autor")
        print("2. Agregar libro")
        print("3. Mostrar información")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        print()

        if opcion == "1":
            agregar_autor()
        elif opcion == "2":
            agregar_libro()
        elif opcion == "3":
            mostrar_informacion()
        elif opcion == "4":
            print("Saliendo del programa... 👋")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.\n")

# Ejecutar programa
menu()
