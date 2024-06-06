#Variables con snakeCase"
#Python realmente no tiene constantes. Todo son variables.
my_variable = "Mi variable."
#Por convención podemos indicar una constante escribiéndolo en mayúsculas. Pero sólo es una convención.
MY_CONSTANTE = "Simulo una constante."

my_int = 1
my_float = 1.5
my_bool = True
my_bool = False
my_string = "Mi cadena de texto"
my_other_string = 'Mi otra cadena de texto'

print("¡Hola, Python!")

print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))

### OPERACIONES
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"División: 10 + 3 = {10 / 3}")
print(f"Resto: 10 mod 3 = {10 % 3}")
print(f"Exponente: 10 + 3 = {10 ** 3}")
print(f"División entera: 10 + 3 = {10 // 3}")

# OPERADORES DE COMPRACIÓN
print(f"IGUALDAD: 10 = 3 = {10 == 3}")
print(f"DESIGUALDAD: 10 != 3 = {10 != 3}")
print(f"MAYOR QUE: 10 > 3 = {10 > 3}")
print(f"MENOR QUE: 10 < 3 = {10 < 3}")
print(f"MAYOR O IGUAL QUE: 10 >= 3 = {10 >= 3}")
print(f"mENOR O IGUAL QUE: 10 <= 3 = {10 <= 3}")

# OPERADORES LÓDICOS
print(f"AND &&: 10 + 3 == 13 AND 5 - 1 = 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR &&: 10 + 3 == 13 OR 5 - 1 = 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 14 OR 5 - 1 = 5 es {10 + 3 == 14 and 5 - 1 == 5}")
print(f"NOT !: NOT 10 + 3 == 14 es {10 + 3 != 14}")

# OPERADORES DE ASIGNACIÓN
my_number = 11 # asignación
print(my_number)
my_number += 1 # suma y asignación
print(my_number)
my_number -= 1 # resta y asignación
print(my_number)
my_number *= 2 # multiplicación y asignación
print(my_number)
my_number /= 2 # división y asignación
print(my_number)
my_number %= 2 # resto y asignación
print(my_number)
my_number **= 1 # esponente y asignación
print(my_number)
my_number //= 1 # división entera y asiganacióm
print(my_number)

# OPERADORES DE IDENTIDAD (comparamos los objetos)
my_new_number = 1.0
print(f"my number is my_new_number es {my_number is my_new_number}")
my_new_number = my_number
print(f"my number is my_new_number es {my_number is my_new_number}")
print(f"my number is not my_new_number es {my_number is not my_new_number}")

# OPERADORES DE PERTENENCIA
print(f"a in Pablo = {'a' in 'Pablo'}")
print(f"a not in Pablo = {'a' not in 'Pablo'}")

# OPERADORES DE BIT (poco usados)
a = 10 # Valor en bits = 1010
b = 3 # Valor en bits = 0011
print(f"AND: 10 & 3 = {a & b}") # compramos bit a bit 0010, por eso da 2.
print(f"OR: 10 & 3 = {a | b}") # compramos bit a bit 1011, por eso da 11.
print(f"XOR: 10 ^ 3 = {a ^ b}") # compramos bit a bit 1001, por eso da 9.
print(f"NOT: ~10 = {~a }") # negamos bit a bit.
print(f"Desplazamiento a la derecha 10 >> 2 = {10 >> 2 }") # 0010
print(f"Desplazamiento a la izquierda 10 << 2 = {10 << 2 }") # 101000

### ESTRUCTURAS DE CONTROL

# CONDICIONALES
my_string = "PabloDev"

if my_string == "Dev":
    print("True")
elif my_string == "PabloDev":
    print ("No es Dev")
else:
    print("No es Dev ni PabloDev")

# ITERATIVAS
for i in range(5):
    print(i)

i=0
while i<=5:
    print(i)
    i +=1

# Manejo de excepciones.
try:
    print(5/0)
except:
    print("No se divide entre 0.")
finally:
    print("Finalizado el manejo de expeciones.")

"""
DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.  
"""
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0: 
        print(num)







