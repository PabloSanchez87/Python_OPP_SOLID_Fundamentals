"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""
# Primer acercamiento.
def fibonacci():
    f = 0
    b = 0
    aux=0
    count = 0
    while count < 50:
        if f==0:
            print(f)
            count+=1
            f+=1
        if f==1 and b==0:
            print(f)
            count+=1
            b=1
        if f>=1 and b<f:
            print(f)
            count+=1
            aux=f
            f+=b
            b=aux
        else:
            print(f)
            count+=1 
            f+=b              
# fibonacci()

# Lógica muy simplificada.
def fibonacci_v2():
    f = 0
    b = 1
    count = 0
    while count < 50:
        print(f)
        f, b = b, f + b  # usamos asignación múltiple para poder hacerlo en una línea, sino tendríamos 
        # aux = f          que usar una variables aux.
        # f = b   
        # b = aux + b  
        count += 1
# fibonacci_v2()


# Una función para que puedes decir cuantos números de la secuencia quieres. 
# Usándo una lista.
def fibonacci_v3(n):
    fibo = [0, 1]  # Inicializamos la lista con los dos primeros números de Fibonacci
    for i in range(2, n):
        fibo.append(fibo[-1] + fibo[-2])  # Añadimos el siguiente número como la suma de los dos anteriores
    return print(fibo)

fibonacci_v3(50)

# RECURSIVIDAD

def fibonacci_v4_recursiva(n):
    if n <= 1:
        return n
    else:
        return fibonacci_v4_recursiva(n-1) + fibonacci_v4_recursiva(n-2)
    
def print_fibo(n):
    for i in range(n):
        print(fibonacci_v4_recursiva(i), end= " ")
    print()

print_fibo(20)

# v2_Recursividad
def fibonacci_recursivo(n, a=0, b=1):
    if n == 0:
        return
    print(a, end= " ")
    fibonacci_recursivo(n-1, b, a+b)

fibonacci_recursivo(50)

