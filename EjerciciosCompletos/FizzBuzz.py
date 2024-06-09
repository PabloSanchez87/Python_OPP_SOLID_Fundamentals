"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
# Múltiplos de 3 por la palabra "fizz".
def fizz(n):
    if n % 3 == 0:
        return True
    return False
# Múltiplos de 5 por la palabra "buzz".
def buzz(n):
    if n % 5 == 0:
        return True
    return False
# Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
            return True 
    return False

# Función principal.
def main():
    for n in range(1,101):
        if fizzbuzz(n):
            print("fizbuzz") 
        elif fizz(n):
            print("fizz")
        elif buzz(n):
            print("buzz")
        else:
            print(n)

main()

