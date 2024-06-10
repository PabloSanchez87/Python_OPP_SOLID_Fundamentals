"""
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
"""
"""
0-1
1-1
2-10
3-11
4-100
5-101
6-110
7-111
8-1000
9-1001
10-1010
11-1011
12-1100
13-1101
14-1110
15-1111
"""

def decimal_to_binary(n):
    binary = ""
    if n==0:
        return "0"
    
    while (n != 0):
        r = n % 2
        n //= 2
        binary = str(r) + binary
    
    return binary

print(decimal_to_binary(0))
print(decimal_to_binary(1))
print(decimal_to_binary(2))
print(decimal_to_binary(5))
print(decimal_to_binary(7))
print(decimal_to_binary(14))


# Con método.
print("·"*5)

print(bin(5)[2:]) # salida: 0b101 --> slide [2:] = 101
print(bin(7)[2:])
print(bin(14)[2:])
