# Problema de Gestión de Inventario
"""
Imagina que trabajas en una empresa de logística y tu tarea es desarrollar un
sistema de gestión de inventario. El inventario está representado como una lista
de productos ordenados por sus códigos. Cada producto se describe como un
diccionario con las claves 'codigo' y 'cantidad' .

Tu objetivo es implementar una función recursiva que realice una búsqueda
binaria en este inventario y devuelva la cantidad disponible para un producto
específico, dado su código.

A continuacion un ejemplo de una posible entrada y salida de la solucion:

                Entrada                                       Salida                        
- Inventario de productos (json,dic,etc)     Cantidad disponible para el producto 307:
- Codigo de producto buscado                                    80
"""

## Busqueda binaria - Recursividad
# La búsqueda binaria se basa en el principio de dividir el rango de búsqueda a la mitad.

"""
Funcionamiento de la Búsqueda Binaria
    - Inicio y Fin: Se define un rango inicial que abarca toda la lista, con índices inicio y fin.
    - Punto Medio: Se calcula el índice del punto medio de este rango.
    - Comparación:
        + Si el elemento en el punto medio es igual al elemento buscado, la búsqueda ha terminado.
        + Si el elemento en el punto medio es mayor que el elemento buscado, se repite el proceso 
            en la mitad inferior de la lista (desplazando fin al índice medio - 1).
        + Si el elemento en el punto medio es menor que el elemento buscado, se repite el proceso 
        en la mitad superior de la lista (desplazando inicio al índice medio + 1).
    - Repetición: El proceso se repite hasta que se encuentra el elemento o el rango de búsqueda 
        se reduce a un tamaño no válido (inicio > fin).
"""


def buscar_cantidad_producto(inventario, codigo_producto, inicio=0, fin=None):
    if fin is None:
        fin = len(inventario)-1
        
    # Caso base: Si el rango no es válido
    if inicio > fin:
        return 0
    
    medio = (inicio + fin)//2
    
    #comparamos el código del producto con el código de la posición media
    if inventario[medio]["codigo"] == codigo_producto:
        # caso base
        return inventario[medio]["cantidad"]
    elif inventario [medio]["codigo"] < codigo_producto:
        # el codigo va a estar en el lado derecha del inventario.
        return buscar_cantidad_producto(inventario, codigo_producto, (medio +1), fin)
    else:
        # el código va a a estar en el lado izquierdo del inventario.
        return buscar_cantidad_producto(inventario, codigo_producto, inicio, (medio-1))
    
    
    # Declarar inventario:
    
inventario = [
    {"codigo": 101, "cantidad": 50},
    {"codigo": 204, "cantidad": 30},
    {"codigo": 307, "cantidad": 80},
    {"codigo": 412, "cantidad": 20},
    {"codigo": 515, "cantidad": 40},
    {"codigo": 525, "cantidad": 50},
    {"codigo": 525, "cantidad": 70},
    {"codigo": 545, "cantidad": 64},
    
]

codigo_producto = 307
cantidad_disponible = buscar_cantidad_producto(inventario, codigo_producto)
print(f"Cantidad disponible para el producto '{codigo_producto}': {cantidad_disponible} unidades.")