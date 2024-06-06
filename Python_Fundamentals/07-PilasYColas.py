"""
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""
## PILA/STACK (LIFO - LAST IN FIRST OUT)
stack = []
stack.append("1") #push
stack.append("2") #push
stack.append("3")

# pop. Ejemplo manual y nativo de las listas de python.
stack_item = stack[len(stack)-1]
del stack[len(stack)-1]
print(stack_item)
print(stack)

print(stack.pop()) # La lista internamente es una PILA. Pop saca el último de la pila
print(stack)

## FIFO/QUEUE (FIST IN - FIRST OUT)
queue =[]
# enqueue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
# dequeue
# pop no valdría pq sacaría el último como en la pila.
# queue.pop()
print(queue.pop(0)) # debemos recalcarle que queremos que saque el primer elemento
print(queue)
print(queue.pop(0)) # debemos recalcarle que queremos que saque el primer elemento
print(queue)

### EXTRA ###
# Simulación navegación web con una pila.
def web_nav():
    stack = []
    while True:
        action = input("Añade una url o interactúa con adelante/atrás/salir: ")
        if action == "salir":
            print("Saliendo del navegador.")
            break
        elif action == "adelante": # Con una pila no podemos ir hacia adelante. La navegación funciona como una lista.
            pass
        elif action == "atrás":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack)-1]}")    
        else:
            print("Estás en la home.")

web_nav()

# Usando cola. Simula el funcionamiento de una impresora compartida.

def shared_printer():
    queue = []

    while True:
        action = input("Añade un documento o selecciona imprimir/salir: ")

        if action == "salir":
            print("Saliendo de la impresora")
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
        else: 
            queue.append(action)

        print(f"Cola de impresión: {queue}")

shared_printer()