"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

" Complidad temporal: 0(n log n) | Complejidad espacial: 0(n)" 
# Usando sorted. Ordenamos y comparamos. Tmb comprobamos que no sean la misma palabra
def anagram_sorted(w1:str, w2:str) -> bool:
    return (sorted(w1) == sorted(w2)) and (len(w1) == len(w2)) and (w1 != w2)



" Complidad temporal: 0(n^2) | Complejidad espacial: 0(n)" 
def anagram_with_lists(w1:str, w2:str) -> bool:
    if len(w1) != len(w2): # Comprobamos que tengan la misma longitud.
        return False

    if w1 == w2: # Comprobamos que no sean iguales.
        return False
    
    list_w2 = list(w2)
    for char in w1: # Recorremos cada letra de la primera palabra
        if char in list_w2: # Intentamos encontrar y eliminar la letra en la lista de la segunda palabra
            list_w2.remove(char) # Eliminamos la letra de la segunda lista
        else:
            return False # Si la letra no está en la segunda lista, no son anagramas
    # Si hemos eliminado todas las letras correctamente, la lista estaría vacía
    return not list_w2
    
## SORTED    
print("-> SORTED")
print(f'amor, roma --> {anagram_sorted("amor", "roma")}')
print(f'silent, listen --> {anagram_sorted("silent", "listen")}')
print(f'hola, hola --> {anagram_sorted("hola", "hola")}')
print(f'casa, cosa --> {anagram_sorted("casa", "cosa")}')
print(f'qwerty, qwert --> {anagram_sorted("qwerty", "qwert")}')
print("-"*40)

### USANDO LISTAS.
print("-> LIST")
print(f'amor, roma --> {anagram_with_lists("amor", "roma")}')
print(f'silent, listen --> {anagram_with_lists("silent", "listen")}')
print(f'hola, hola --> {anagram_with_lists("hola", "hola")}')
print(f'casa, cosa --> {anagram_with_lists("casa", "cosa")}')
print(f'qwerty, qwert --> {anagram_with_lists("qwerty", "qwert")}')

print("-"*40)
# Prueba para el usuario.
while True:
    w1 = input("Introduzca la primera palabra: ")
    w2 = input("Introduzca la segunda palabra: ")
    print(f"  · ¿Son anagrmas? {anagram_sorted(w1,w2)}")
    control = input("¿Quieres introducir más palabras? (s/n): ").strip().lower()
    if control != 's':
        print("Adiós!")
        break
       




    


