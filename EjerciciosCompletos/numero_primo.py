"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_prime(n):
    if n <=1:
        return f"El {n} NO es primo."
    for i in range(2, n):
        if n % i == 0:
            return f"El {n} NO es primo."
    return f"El {n} es primo."
    
       
for number in range(101):
    print(is_prime(number))


