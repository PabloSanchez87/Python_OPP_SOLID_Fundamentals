"""
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""

#EJERCICIO:
#   Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
#   números del 1 al 10 mediante iteración.

# Option 1: For
for i in range(1, 11):
    print(i)

# Option 2: While
i=1
while i<=10:
    print(i)
    i += 1

# Option 3: Recursividad
def count_ten(i:1):
    print(i)
    if(i<10): count_ten(i+1)

count_ten(1)


###############
##   EXTRA   ##
###############

# DIFICULTAD EXTRA (opcional):
#   Escribe el mayor número de mecanismos que posea tu lenguaje
#   para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?

# 3 - For, While y Recursividad anteriores.

for e in [1,2,3,4]:
    print(e)

for e in {1,2,3,4}:
    print(e)

# Map
for e in {1:"a", 2:"b", 3:"c", 4:"d"}:
    print(e)

# Map
for e in {1:"a", 2:"b", 3:"c", 4:"d"}.values():
    print(e)

# Map
for e in {1:"a", 2:"b", 3:"c", 4:"d"}.keys():
    print(e)    

# Compresionlist
print(*[e for e in range(1,11)], sep="\n" )

for e in "Python":
    print(e)

for e in "Python":
    print(e)

for e in reversed([1,2,3,4]):
    print(e)

for e in sorted(["p", "a", "b", "l", "o"]):
    print(e)

for i, e in enumerate(sorted(["p", "a", "b", "l", "o"])):
    print(f"Índice: {i}, Valor: {e}")