"""
Recursividad.
Tienes a tu disposición un conjunto de discos numerados del 1 al N y tres torres
etiquetadas como A, B y C. La torre A contiene inicialmente todos los discos
apilados en orden descendente, desde el disco N en la parte inferior hasta el
disco 1 en la parte superior.

Tu tarea es implementar una solución recursiva para mover todos los discos
desde la torre A hasta la torre C, siguiendo las reglas clásicas de las Torres de
Hanoi:
    1. Puedes mover un disco a una torre adyacente.
    2. Solo puedes mover un disco a la cima de otra pila si esa pila está vacía o si
        el disco superior es más grande que el disco que estás colocando.
        
Debes definir una función llamada torres_de_hanoi(n, origen, destino, auxiliar)
que, dado el número total de discos n y las torres de origen, destino y auxiliar,
imprima los pasos necesarios para lograr el movimiento de todos los discos
desde la torre A hasta la torre C.

    Entrada                                             Salida
- N de discos                           Mover disco de la torre A a la torre D
- N de torres                           Mover disco de la torre A a la torre B
- Torres : origen, desitno, auxiliar    …
"""

# Versión inicial.
"""
def mover_disco(desde, hacia, disco):
    print(f"Mover disco {disco} de la torre {desde} hacia la torre {hacia}")
    
def torres_de_hanoi(n, origen, destino, auxiliar):
    # Caso base
    if n==1:
        mover_disco(origen, destino, n)
        return
    torres_de_hanoi(n-1, origen, auxiliar, destino)
    mover_disco(origen, destino, n)
    torres_de_hanoi(n-1,auxiliar,destino,origen)        
    
torres_de_hanoi(3,"Origen", "Destino", "Auxiliar")
"""

## Versión mejorada.
def inicializar_torres(n):
    origen = list(range(n, 0, -1))          # Torre inicial con discos del 1 al n
    auxiliar = []                           # Torre auxiliar vacía
    destino = []                            # Torre destino vacía
    torres = [origen, auxiliar, destino]
    print(torres)
    return torres

def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        # Movimiento directo del disco de origen a destino
        destino.append(origen.pop())
        # Imprimir estado actual de las torres
        print(torres)
        return
    
    # Mover n-1 discos de origen a auxiliar usando destino como auxiliar
    hanoi(n-1, origen, destino, auxiliar)
    # Mover el disco restante de origen a destino
    destino.append(origen.pop())
    # Imprimir estado actual de las torres
    print(torres)
    # Mover n-1 discos de auxiliar a destino usando origen como auxiliar
    hanoi(n-1, auxiliar, origen, destino)



## Ejecución principal.
while True:
    try:
        # Obtener el número de discos
        n = (input("Introduzca el número de discos con los que desea jugar('S' para salir): "))
        if n.lower() != "s":
            # Inicializar las torres según el número de discos
            torres = inicializar_torres(int(n))
            # Llamar a la función hanoi para resolver el problema
            hanoi(int(n), torres[0], torres[1], torres[2])
        else:
            break
    except ValueError:
        pass