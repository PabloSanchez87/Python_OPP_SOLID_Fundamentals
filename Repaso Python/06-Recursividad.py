"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""
## RECURSIVIDAD
# Función que se llama a ella misma.

# Ejemplo sencillo.
def countdown(number:int):
    if number >= 0:
        print(number)
        countdown(number-1)

#countdown(5)

### EXTRA ###
def factorial(number:int) -> int:
    if number < 0:
        print("Número negativo no es válido.")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))

## Fibonacci de una posición (suma de las 2 posiciones anteriores).
def fibonacci(number:int) -> int:
    if number <= 0:
        print("Número no es valido.")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1    
    else:
        return fibonacci(number-1)+fibonacci(number-2)
        
print(fibonacci(10))