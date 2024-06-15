import time
import os

def resolver_laberinto(laberinto, fila, columna, camino=None, visitado=None):
    """
    Encuentra la ruta más corta en un laberinto desde una posición inicial hasta la salida.

    Parámetros:
    laberinto (list of list of int): Matriz que representa el laberinto.
    fila (int): Fila inicial.
    columna (int): Columna inicial.
    camino (list of tuple): Ruta actual tomada (por defecto es None, se inicializa como lista vacía).
    visitado (set of tuple): Conjunto de posiciones visitadas (por defecto es None, se inicializa como set vacío).

    Retorna:
    list of tuple: Lista de coordenadas que representan el camino desde la posición inicial hasta la salida.
    None: Si no hay solución.
    """
    if camino is None:
        camino = []
    if visitado is None:
        visitado = set()

    # Restricción de avance: fuera de los límites, pared o ya visitado.
    if not(0 <= fila < len(laberinto)) or not (0 <= columna < len(laberinto[0])) or laberinto[fila][columna] == 1 or (fila, columna) in visitado:
        return None

    # Añadir la posición actual al camino y marcar como visitada.
    camino.append((fila, columna))
    visitado.add((fila, columna))

    # Imprimir el laberinto actualizado.
    imprimir_laberinto(laberinto, camino)
    time.sleep(0.5)  # Añadir un retraso para la animación.

    # Caso base: verificar si hemos llegado a la salida.
    if laberinto[fila][columna] == 9:
        return camino

    # Definir los movimientos posibles: arriba, abajo, izquierda, derecha.
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Intentar cada movimiento recursivamente.
    for movimiento in movimientos:
        nueva_fila, nueva_columna = fila + movimiento[0], columna + movimiento[1]
        resultado = resolver_laberinto(laberinto, nueva_fila, nueva_columna, camino, visitado)
        if resultado:
            return resultado

    # Si ningún movimiento lleva a una solución, retroceder y eliminar la posición actual del camino.
    camino.pop()
    visitado.remove((fila, columna))
    return None

def imprimir_laberinto(laberinto, camino):
    """
    Imprime el laberinto con el camino encontrado marcado por asteriscos.

    Parámetros:
    laberinto (list of list of int): Matriz que representa el laberinto.
    camino (list of tuple): Ruta encontrada desde la posición inicial hasta la salida.
    """
    # Limpiar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear') # nt -> Windows // posix -> linux/macOS

    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            if (fila, columna) in camino:
                print('*', end=' ')
            else:
                print(laberinto[fila][columna], end=' ')
        print()

# Definición del laberinto como una matriz.
laberinto = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 9, 1]
]

# Llamada a la función para resolver el laberinto desde la posición (0, 0).
camino_solucion = resolver_laberinto(laberinto, 0, 0)

# Imprimir el resultado final.
if camino_solucion:
    print("El camino para salir del laberinto es:")
    imprimir_laberinto(laberinto, camino_solucion)
else:
    print("No hay solución para este laberinto.")
