"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""
# Partiendo de valores iniciales igual a 0.
def fibonacci():
    f = 0
    b = 0
    aux=0
    count = 0
    while count < 50:
        if f==0:
            print(f, end= " ")
            count+=1
            f+=1
        if f==1 and b==0:
            print(f,end= " ")
            count+=1
            b=1
        if f>=1 and b<f:
            print(f, end= " ")
            count+=1
            aux=f
            f+=b
            b=aux
        else:
            print(f, end= " ")
            count+=1 
            f+=b 
    print()

print("VERSIÓN 1: ")
fibonacci()
print("-"*100) 

# Simplifico la primera versión
def fibonacci_v2():
    f = 0  # Primer valor de la secuencia
    b = 0  # Segundo valor de la secuencia (inicialmente también 0)
    count = 0
    while count < 50:
        print(f, end=" ")
        # Manejar el caso especial cuando ambos son 0
        if f == 0 and b == 0:
            f = 1  # Pasar a 1 para la siguiente iteración
        else:
            aux = f + b
            b = f
            f = aux
        count += 1
    print()

print("VERSIÓN 2: ")
fibonacci_v2()
print("-" * 100)



# Lógica muy simplificada dándole a b valor 1 inicialmente.
def fibonacci_v3():
    f = 0
    b = 1
    count = 0
    while count < 50:
        print(f, end= " ")
        f, b = b, f + b  # usamos asignación múltiple para poder hacerlo en una línea, sino tendríamos 
        # aux = f          que usar una variables aux.
        # f = b   
        # b = aux + b  
        count += 1
    print() 

print("VERSIÓN 3: ")
fibonacci_v3()
print("-"*100) 


# Una función para que puedes decir cuantos números de la secuencia quieres. 
# Usándo una lista.
def fibonacci_v4(n):
    fibo = [0, 1]  # Inicializamos la lista con los dos primeros números de Fibonacci
    for i in range(2, n):
        fibo.append(fibo[-1] + fibo[-2])  # Añadimos el siguiente número como la suma de los dos anteriores
    return print(fibo)

print("VERSIÓN 4: ")
fibonacci_v4(50)
print("-"*100)


# Recursividad
def fibonacci_recursivo(n, a=0, b=1):
    if n == 0:
        return
    print(a, end= " ")
    fibonacci_recursivo(n-1, b, a+b)

print("VERSIÓN RECURSIVA: ")
fibonacci_recursivo(50)
print()
print("-"*100)


## Prueba con YIELD
## Mostrando los números según se lo pedimos.
#       La SENTENCIA YIELD se utiliza en Python dentro de una función para convertirla en un GENERADOR. 
#       Los generadores son funciones especiales que permiten producir una secuencia de valores de manera paulatina, 
#       manteniendo su estado entre llamadas sucesivas. Cuando una función generadora es llamada, devuelve un objeto 
#       generador sin ejecutar el cuerpo de la función. El cuerpo de la función solo se ejecuta cuando se invoca el 
#       método __next__() (o la función NEXT()) en el objeto generador.

def fibonacci_yield():
    f, b = 0, 1
    while True:
        yield f
        f, b = b, f + b

def show_fibonacci():
    fibo = fibonacci_yield()
    while True:
        try:
            count = int(input("¿Cuántos números de la secuencia de Fibonacci quieres ver? (Ingresa 0 para salir): "))
            if count == 0:
                print("Saliendo...")
                break
            for _ in range(count):
                print(next(fibo), end=" ")
            print()  # Nueva línea después de imprimir los números
            more = input("¿Quieres ver más números? (s/n): ").strip().lower()
            if more != 's':
                print("Adiós!")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Llamar a la función para iniciar la interacción
show_fibonacci()