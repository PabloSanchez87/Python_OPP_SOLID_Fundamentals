"""
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
"""

text = "Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas. Los signos de puntuación no forman parte de la palabra. Una palabra es la misma aunque aparezca en mayúsculas y minúsculas. No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente."

## Aquí sólo he controlado el espacio y el . como signos.
import re

list_word = []
word = ""
for char in text.lower():
    if char not in r'[.,;:-_()!"¡ç¡¿?&%$ªº*= ]':
        word = word + char
    elif word != "":
        list_word.append(word)
        word = ""

print(list_word)

# Usamos un diccionario.
word_counter = {}
for word in list_word:
    if word in word_counter:
        word_counter[word]+=1
    else:
        word_counter[word]=1

# Imprimirmos el resultado del diccionario.
for word, count in word_counter.items():
    print(f"La contador de {word}: {count}")     

#############################
## USANDO COLLECTION.COUNTER.
#############################

import re
from collections import Counter
print("·"*40)
words = []

# Convertir todo el texto a minúsculas y eliminar signos de puntuación Después hacemos un split para dividir el texto en palabras.
words = re.sub(r'[.,;:!?\(\)\[\]\{\}\"\¡\¿\&\%\$\ª\º\*\=]', '',text.lower()).split()
        # re.sub (pattern, reemplazo, cadena) ->str
        
# Usar Counter para contar la frecuencia de cada palabra
word_counter = Counter(words)

# Imprimir el resultado del diccionario
for word, count in word_counter.items():
    print(f"La contador de {word}: {count}")





    