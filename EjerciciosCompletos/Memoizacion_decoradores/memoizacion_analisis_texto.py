# Ejercicio de Memoización en Análisis de Texto
"""
Imagina que estás trabajando en un sistema de análisis de texto que requiere
calcular la frecuencia de ocurrencia de palabras en un conjunto de
documentos. 
Implementa una función llamada calcular_frecuencia_palabras que
tome como entrada un texto y devuelva un diccionario que muestre la
frecuencia de cada palabra en el texto.

    1. La función debe ser capaz de manejar textos y ser insensible a
            mayúsculas/minúsculas (por ejemplo, "Hola" y "hola" se consideran la
            misma palabra).
    2. Se deben excluir las palabras comunes (artículos, preposiciones, etc.) que
            no aportan información relevante al análisis.
    3. Utiliza memoización para evitar recalcular la frecuencia de palabras para el
            mismo texto.
"""

import functools
import re
import time

@functools.lru_cache(maxsize=None)
def calcular_frecuencia_palabras(text):
    # Procesamiento del texto
    text = text.lower()
    #Eliminar puntuacion o caracteres no deseados
    text = re.sub(r'[^a-z\s]', "", text)
    words = text.split()
    
    # Excluir palabras comunes
    common_words = set(["el", "la", "los", "las", "de", "en", "y", 
                        "a", "con", "es", "un", "una", "para"])
    words = [word for word in words if word  not in common_words]
    
    #Frecuencia palabra.
    hz = {}
    
    for word in words:
        hz[word] = hz.get(word, 0)+1
    
    return hz

text_1 = "Este es un ejemplo de análisis de texto. Este texto tiene varias palabras repetidas."
text_2 = "Otro ejemplo de Análisis de texto con palabras repetiras. Ejemplo y texto se repiten."


print("·"*60)
print(" · SIN MEMOIZACION · ")
inicio = time.time()
hz_sin_memo_1 = calcular_frecuencia_palabras(text_1)
# hz_sin_memo_2 = calcular_frecuencia_palabras(text_2)
fin = time.time()
tiempo_total = (fin-inicio)*1_000_000
print(f"Tiempo sin memoización: {tiempo_total:.3f} microsegundos.")

print("·"*60)
print(" · CON MEMOIZACION --> Repitiendo cálculos pero no datos. ·")
inicio_2 = time.time()
#hz_con_memo_1 = calcular_frecuencia_palabras(text_1)
hz_con_memo_2 = calcular_frecuencia_palabras(text_2)
fin_2 = time.time()
tiempo_total_2 = (fin_2-inicio_2)*1_000_000
print(f"Tiempo con memoización: {tiempo_total_2:.3f} microsegundos.")

print("·"*60)
print(" · CON MEMOIZACION --> Repitiendo cálculos y datos. ·")
inicio_3 = time.time()
hz_con_memo_1 = calcular_frecuencia_palabras(text_1)
hz_con_memo_2 = calcular_frecuencia_palabras(text_2)
fin_3 = time.time()
tiempo_total_3 = (fin_3-inicio_3)*1_000_000
print(f"Tiempo con memoización: {tiempo_total_3:.3f} microsegundos.")

###
# Caso de texto más largo.
long_text = """"En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos los sábados, lantejas los viernes, algún palomino de añadidura los domingos, consumían las tres partes de su hacienda. El resto della concluían sayo de velarte, calzas de velludo para las fiestas, con sus pantuflos de lo mesmo, y los días de entresemana se honraba con su vellorí de lo más fino. Tenía en su casa una ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza, que así ensillaba el rocín como tomaba la podadera. Frisaba la edad de nuestro hidalgo con los cincuenta años; era de complexión recia, seco de carnes, enjuto de rostro, gran madrugador y amigo de la caza. Quieren decir que tenía el sobrenombre de Quijada, o Quesada, que en esto hay alguna diferencia en los autores que deste caso escriben; aunque por conjeturas verosímiles se deja entender que se llamaba Quijana. Pero esto importa poco a nuestro cuento: basta que en la narración dél no se salga un punto de la verdad.
Es, pues, de saber que este sobredicho hidalgo, los ratos que estaba ocioso, que eran los más del año, se daba a leer libros de caballerías, con tanta afición y gusto, que olvidó casi de todo punto el ejercicio de la caza, y aun la administración de su hacienda; y llegó a tanto su curiosidad y desatino en esto, que vendió muchas hanegas de tierra de sembradura para comprar libros de caballerías en que leer, y así, llevó a su casa todos cuantos pudo haber dellos; y de todos, ningunos le parecían tan bien como los que compuso el famoso Feliciano de Silva; porque la claridad de su prosa y aquellas entricadas razones suyas le parecían de perlas, y más cuando llegaba a leer aquellos requiebros y cartas de desafíos, donde en muchas partes hallaba escrito: «La razón de la sinrazón que a mi razón se hace, de tal manera mi razón enflaquece, que con razón me quejo de la vuestra fermosura». Y también cuando leía: «... los altos cielos que de vuestra divinidad divinamente con las estrellas os fortifican, y os hacen merecedora del merecimiento que merece la vuestra grandeza»."""

print("·"*60)
print(" · CON MEMOIZACION --> Texto largo. ·")
inicio_4 = time.time()
hz_sin_memo = calcular_frecuencia_palabras(long_text)
fin_4 = time.time()
tiempo_total_4 = (fin_4-inicio_4)*1_000_000
print(f"Tiempo sin memoización: {tiempo_total_4:.3f} microsegundos.")

inicio_5 = time.time()
hz_con_memo = calcular_frecuencia_palabras(long_text)
fin_5 = time.time()
tiempo_total_5 = (fin_5-inicio_5)*1_000_000
print(f"Tiempo con memoización: {tiempo_total_5:.3f} microsegundos.")