from Contantes import colors
"""
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
"""
# FUNCIONES DE ORDEN SUPERIOR (muy enfocado a la PROGRAMACIÓN FUNCIONAL):
#       · Las funciones de orden superior (o funciones de alto orden) son funciones que pueden 
#           recibir otras funciones como argumentos y/o devolver funciones como resultado. 
#           Estas funciones son una característica fundamental en la programación funcional y 
#           permiten crear programas más flexibles y reutilizables.
#       . CARACTERÍSTICAS:
#           + RECIBEN FUNCIONES COMO PARÁMETROS: Pueden tomar una o más funciones como argumentos.
#           + DEVUELVEN FUNCIONES COMO RESULTADO: Pueden producir una nueva función al finalizar su ejecución.
#           + MEJORAN LA ABSTRACCIÓN: Permiten escribir código más abstracto y reutilizable al eliminar la necesidad de duplicar código.
#           + FACILITAN OPERACIONES COMUNES: Simplifican el uso de patrones de diseño como mapeo, filtrado y reducción de listas o colecciones.

#  * EJERCICIO:
#  * Explora el concepto de funciones de orden superior en tu lenguaje 
#  * creando ejemplos simples (a tu elección) que muestren su funcionamiento.

### FUNCIÓN COMO ARGUMENTO
def apply_func(func, x):
    return func(x)
print(apply_func(len, "Pablo"))

### RETORNO COMO FUNCIÓN
def apply_multiplier(n):
    def multiplier(x):
        return x*n
    return multiplier
# que tipo devuelve.
print(type(apply_multiplier(2)))

multiplier = apply_multiplier(2) # Tenemos seteado el valor de n como contexto.
print(multiplier(3)) # aquí le damos el valor de x
print(apply_multiplier(3)(2)) # Comparación.

### SISTEMA - Ejemplos de funciones predefinidas de orden superior del sistema.

numbers = [3,5,2,4,1]

#map() ----> Le pasamos una lista como argumentos y nos devuelve una nueva lista 
#           que es el resultado de aplicarle a la lista la función que le hemos pasado.

def apply_double(n):
    return n*2
# Nos devuelve un tipo map.
print(type(map(apply_double, numbers)))
# Convertimos el obj tipo map en una lista.
print(list(map(apply_double, numbers)))


#filter() -> Filtra los elementos aplicandole a la lista la función que le pasamos.

def is_even(n):
    return n % 2 == 0
# Nos devuelve un tipo filter.
print(type(filter(is_even, numbers)))
# Convertimos el obj tipo filter en una lista.
print(list(filter(is_even, numbers)))


#sorted() -> Ordena los elementos.

# Según el tipo de dato que le pasemos, si no es complejo le aplica un criterio por defecto.
print(sorted(numbers))
# Podemos pasarle parametro para cambiar el resultado.
print(sorted(numbers, reverse=True))
# Tambien tenemos la key en la que le podríamos pasar una función anónima lambda.
print(sorted(numbers, key=lambda x : -x))


#reduce() -> Recibe un iterable y una función pero devuelve un sólo valor después 
#            de aplicar la función de manera acumulativa.
from functools import reduce # Tenemos que importarla.
from datetime import datetime

def sum_values(x,y):
    return x + y

print(reduce(sum_values, numbers))

                            ###############
                            ##   EXTRA   ##
                            ###############                 
#  * DIFICULTAD EXTRA (opcional):
#  * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
#  * lista de calificaciones), utiliza funciones de orden superior para
#  * realizar las siguientes operaciones de procesamiento y análisis:
#  * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
#  *   y promedio de sus calificaciones.
#  * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
#  *   que tienen calificaciones con un 9 o más de promedio.
#  * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
#  * - Mayor calificación: Obtiene la calificación más alta de entre todas las
#  *   de los alumnos.
#  * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).

students_list = [
    {"name": "Pablo", "birthday": "01-12-1987", "grades": [5, 8.5, 10]},
    {"name": "Laura", "birthday": "05-11-1988", "grades": [8, 9.5, 9]},
    {"name": "David", "birthday": "01-09-1954", "grades": [5.5, 6.5, 8]},
    {"name": "Maria", "birthday": "15-07-1983", "grades": [9.5, 10, 8]}
]


#  * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
#  *   y promedio de sus calificaciones.

# Aquí hemos sido capaces de crear un nuevo mapa con los grades.
print(list(map(lambda student:
                {"name": student["name"], "grades": student["grades"]},
                students_list)))

def average(grades):
    return round(sum(grades) / len(grades), 2)

print(list(map(lambda student: 
               {"name": student["name"], "average": average(student["grades"])}, 
               students_list)))


#  * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
#  *   que tienen calificaciones con un 9 o más de promedio.

print(list(map(lambda student: 
               student["name"], 
               filter(lambda student: average(student["grades"])>=9, 
                      students_list))))


#  * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.

print(sorted(students_list, 
       key=lambda student: 
            datetime.strptime(student["birthday"], "%d-%m-%Y"),
                reverse=True))

#  * - Mayor calificación: Obtiene la calificación más alta de entre todas las
#  *   de los alumnos.

print(max(map(lambda student: 
              max(student["grades"]), students_list)))



