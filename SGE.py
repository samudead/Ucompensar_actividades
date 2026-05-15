# ==========================================
# Sistema de Gestión de Estudiantes (SGE)
# ==========================================

# Lista para almacenar estudiantes
lista_estudiantes = []

# Variable de conteo
contador_estudiantes = 0

# Variable bandera
bandera_salir = False


# ------------------------------------------
# Función para agregar estudiantes
# ------------------------------------------
def agregar_estudiante():
    global contador_estudiantes

    print("\n--- AGREGAR ESTUDIANTE ---")

    try:
        id_estudiante = int(input("Ingrese ID: "))
        nombre = input("Ingrese nombre: ")
        edad = int(input("Ingrese edad: "))

        estudiante = {
            "id": id_estudiante,
            "nombre": nombre,
            "edad": edad
        }

        lista_estudiantes.append(estudiante)

        contador_estudiantes += 1

        print("Estudiante agregado correctamente.")

    except ValueError:
        print("Error: Debe ingresar datos válidos.")


# ------------------------------------------
# Función para mostrar estudiantes
# ------------------------------------------
def mostrar_estudiantes():

    print("\n--- LISTA DE ESTUDIANTES ---")

    if len(lista_estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:

        for estudiante in lista_estudiantes:

            print("---------------------")
            print(f"ID: {estudiante['id']}")
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Edad: {estudiante['edad']}")

        print("---------------------")
        print(f"Total estudiantes: {contador_estudiantes}")


# ------------------------------------------
# Función para buscar estudiante por ID
# ------------------------------------------
def buscar_estudiante():

    print("\n--- BUSCAR ESTUDIANTE ---")

    try:
        id_busqueda = int(input("Ingrese el ID a buscar: "))

        encontrado = False

        for estudiante in lista_estudiantes:

            if estudiante["id"] == id_busqueda:

                print("\nEstudiante encontrado:")
                print(f"ID: {estudiante['id']}")
                print(f"Nombre: {estudiante['nombre']}")
                print(f"Edad: {estudiante['edad']}")

                encontrado = True
                break

        if not encontrado:
            print("No se encontró ningún estudiante.")

    except ValueError:
        print("Error: Debe ingresar un número válido.")


# ------------------------------------------
# Programa principal
# ------------------------------------------
while not bandera_salir:

    print("\n=================================")
    print(" SISTEMA DE GESTIÓN ESTUDIANTIL ")
    print("=================================")

    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:

        case "1":
            agregar_estudiante()

        case "2":
            mostrar_estudiantes()

        case "3":
            buscar_estudiante()

        case "4":
            print("Saliendo del sistema...")
            bandera_salir = True

        case _:
            print("Opción inválida.")