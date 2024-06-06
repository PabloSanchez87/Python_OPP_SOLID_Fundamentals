"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""

### ESTRUCTURA DE DATOS.

# LISTAS
my_list = ["Pablo", "Sanchez", "Torres", "Laura", "Asorey", "Souto"]
print(my_list)
# Añadimos un dato nuevo
my_list.append("Pau")
my_list.append("David")
print(my_list)
# Borramos un dato
my_list.remove("Souto")
print(my_list)
# Acceso posicón e actulización
my_list[2] = "Roi"
print(my_list)
# Ordenar la lista
my_list.sort()
print(my_list)
print(type(my_list))

# TUPLAS (inmutabilidad)
my_typle = ("Pau", "David", "Roi", "Anton", "4")
print(my_typle)
print(type(my_typle))
# Acceso 
print(my_typle[2])
# Ordenación con sorted. SORTED NOS DEVUELVE UNA LISTA!!!
my_typle = tuple(sorted(my_typle)) ## Tenemos que transformar la lista resultante en un tupla.
print(my_typle)

# SETS --> Es una estructura desordenada. No nos podemos fiar de su posición.
# Transforma los datos en un hash para optimizar. No se puede ordenar.
my_set = {"Pau", "David", "Roi", "Anton", "4"}
print(type(my_set))
print(my_set)
# Añadimos un dato
my_set.add("Pablo")
my_set.add("Laura")
print(my_set)
my_set.add("Pablo") # No guarda datos duplicados. Es más óptimos ya que no lo tenemos que controlar.
print(my_set)
# Borrar un datos
my_set.remove("Laura")
print(my_set)
# Update. No cambia un dato por otro. Amplia los datos del set.
# Ordenación
my_set = sorted(my_set) # Lo ordena trasformado en una lista.
print(type(my_set))
print(my_set)

# Diccionario. Clave-valor. Es ordenado en python pero por decisión del lenguaje no por fundamental.
my_dict ={
    "name" : "Pablo",
    "apellido" : "Sánchez",
    "alias" : "Pablost"
}
print(type(my_dict))
print(my_dict)
# Acceso datos.
print(my_dict["name"])
# Añadir un valor
my_dict["email"] = "@sanchez"
print(my_dict)
# Actulizar
my_dict["email"] = "@sanchezTorresPablo"
print(my_dict)
# Eliminar datos.
del my_dict["email"]
print(my_dict)
# Ordenar.
my_dict = dict (sorted(my_dict.items())) # Sorted nos devuelve una lista de tuplas clave-valor ordenada. Debemos convertirla en un diccionario de nuevo
print(my_dict)
print(type(my_dict))

### EXTRA ###
def my_agenda():

    agenda = {}
    
    while True:
        print("\n1.Buscar contacto")
        print("2.Insertar contacto")
        print("3.Actualizar contacto")
        print("4.Eliminar contacto")
        print("5.Salir.")

        option = (input("\nSeleccionar una opción: "))

        match option:
            case "1":
                name = (input("\nIntroduce el nombre a buscar: "))
                if name in agenda:
                    print(f"El número de teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El nombre  {name} no existe.")
            case "2":
                name = (input("\nIntroduce el nombre: "))
                phone = (input("\nIntroduce el teléfono: "))
                if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                    agenda[name] = phone
                else:
                    print("Debes introducir un número de teñefono entre 0 y 11 dígitos.")
            case "3":
                name = (input("\nIntroduce el nombre a actualizar: "))
                if name in agenda:
                    phone = (input("\nIntroduce el teléfono: "))
                    if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                        agenda[name] = phone
                    else:
                        print("Debes introducir un número de teñefono entre 0 y 11 dígitos.")
                else:
                    print(f"El nombre  {name} no existe.")
            case "4":
                name = (input("\nIntroduce el nombre a eliminar: "))
                if name in agenda:
                    del agenda[name]
                    print(f"El contacto {name} ha sido eliminado.")
                else:
                    print(f"El nombre  {name} no existe.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida. Por favor introduzca del 1 al 5.")

my_agenda()

