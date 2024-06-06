"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
"""
## MANEJO DE FICHEROS
import os

filename = "texto.txt"
with open (filename,"w") as file: # w, permiso sólo de escritura.
    file.write("Pablo\n")           # haciéndolo así solo tenemos acceso al file en este scope.
    file.write("36\n")
    file.write("Python")

with open(filename, "r") as file: # r, permiso de lectura
    print(file.read())              # haciéndolo así solo tenemos acceso al file en este scope.

os.remove(filename)

print("")


### EXTRA ###

file_name = "inventario.txt"
open(file_name, "a") # a, para añadir (append)

def menu():
    print("")
    print("1. Añadir producto.")
    print("2. Consultar producto.")
    print("3. Actualizar producto.")
    print("4. Borrar producto.")
    print("5. Mostrar productos.")
    print("6. Calcular venta total.")
    print("7. Calcular venta por producto.")
    print("8. Salir.")
    option = input("Selecciona una opcion: ")
    return option

def add_product():
    print("Añadir producto.")
    name = input("Nombre: ")
    quantity = input("Cantidad: ")
    price = input("Precio: ")

    with open(file_name, "a") as file: # a, para añadir (append)
        file.write(f"{name}, {quantity}, {price}\n")

def seach_product():
    print("Consultar producto.")
    name = input("  Nombre a buscar: ")
    with open(file_name, "r") as file:
        for line in file.readlines():
            if line.split(", ")[0] == name:
                print("\n       ", line)
                break
        else:
            print(" No se ha encontrado ese producto.")

def show_file():
    with open(file_name, "r") as file:
        print(file.read())

def exit():
    print("Saliendo del programa y eliminando archivo.\n")
    os.remove(file_name)

def update_product():
    print("Actualizar producto.\n")
    name = input("Nombre: ")
    quantity = input("Cantidad: ")
    price = input("Precio: ")

    with open(file_name, "r") as file: # Guardamos una copia de las lineas del archivo.
        lines = file.readlines()
    
    with open(file_name, "w") as file: # Buscamos en las líneas una coincidencia para escribir los nuevos datos, y sino guardamos la linea como estaba.
        for line in lines:
            if line.split(", ")[0] == name:
                file.write(f"{name}, {quantity}, {price}\n")
            else:
                file.write(line)
                    
def remove_product():
    print("Borrar producto.\n")
    name = input("Nombre: ")

    with open(file_name, "r") as file: # Guardamos una copia de las lineas del archivo.
        lines = file.readlines()
    
    with open(file_name, "w") as file: # Buscamos en las líneas una coincidencia para escribir los nuevos datos, y sino guardamos la linea como estaba.
        for line in lines:
            if line.split(", ")[0] != name:
                file.write(line)
                   
def total():
    total = 0
    with open(file_name, "r") as file: # Guardamos una copia de las lineas del archivo.
        for line in file.readlines():
            values = line.split(", ")
            quantity = int(values[1])
            price = float(values[2])
            total += quantity*price
    print(f"Total de ventas: {total}")

def total_product():
    total = 0
    print("Consultar total por producto.")
    name = input("  Nombre a buscar: ")
    with open(file_name, "r") as file: # Guardamos una copia de las lineas del archivo.
        for line in file.readlines():
            values = line.split(", ")
            if values[0] == name:
                quantity = int(values[1])
                price = float(values[2])
                total += quantity*price
                break
    print(f"\nTotal de ventas de {name} es: {total}")

while True:
    option = menu()
    print("")

    match option:
        case "1": # Añadir producto
            add_product()
        case "2": # Consultar producto
            seach_product()            
        case "3": # Actualizar producto 
            update_product()
        case "4": # Borrar producto
            remove_product()
        case "5": # Mostrar producto
            show_file()
        case "6": # Calcular venta total
            total()
        case "7": # Calcular venta por producto
            total_product()
        case "8": # Salir.
            exit()
            break
        case _:
            print("Opción no válida. Por favor introduzca del 1 al 7.")
