"""
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
"""

# * EJERCICIO:
#  * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
#  * operaciones (debes utilizar una estructura que las soporte):
#  * - Añade un elemento al final.
#  * - Añade un elemento al principio.
#  * - Añade varios elementos en bloque al final.
#  * - Añade varios elementos en bloque en una posición concreta.
#  * - Elimina un elemento en una posición concreta.
#  * - Actualiza el valor de un elemento en una posición concreta.
#  * - Comprueba si un elemento está en un conjunto.
#  * - Elimina todo el contenido del conjunto.

text = "Lista."
data = [1,2,3,4,5]
print(text, data)

text= "Añade un elemento al final."
data.append(6)
print(text, data)

text = "Añade un elemento al principio."
data.insert(0,0)
print(text, data)

text = "Añade varios elementos en bloque al final."
data.extend([7,8,9])
print(text, data)

text = "Añade varios elementos en bloque en una posición concreta."
data[3:3] = [-1,-2,-3] # SLIDES
print(text, data)

text = "Elimina un elemento en una posición concreta."
del data[3] # Eliminamos la posición 3
print(text, data)

text = "Actualiza el valor de un elemento en una posición concreta."
data[4] = -1 
print(text, data)

print(f"Comprobar si un elemento está en el conjunto:  {-1 in data}")
print(f"Comprobar si un elemento está en el conjunto:  {-5 in data}")
print(text, data)

text = "Elimina todo el contenido del conjunto."
# del data
data.clear()
print(text, data)


                    ###############
                    ##   EXTRA   ##
                    ###############

# * DIFICULTAD EXTRA (opcional):
#  * Muestra ejemplos de las siguientes operaciones con conjuntos:
#  * - Unión.
#  * - Intersección.
#  * - Diferencia.
#  * - Diferencia simétrica.

set_1 = {1,2,3,4,5}
set_2 = {1,2,3,4,5,6,7,8}

# Union guarda los elementos sin repetir.
text = "Unión"
union = set_1.union(set_2)
print(text,union)

# Intersection guarda los elementos que están en ambas listas de forma única
set_1 = {1,2,3,4,5}
set_2 = {1,2,3,4,6,7,8}
text = "Intersección."
intersection = set_1.intersection(set_2)
print(text,intersection)

# Diferencia. Elementos distintos de un elemento respecto al otro.
text = "Diferencia."
diff = set_1.difference(set_2)
print(text,diff)
diff = set_2.difference(set_1)
print(text,diff)

# Diferencia simétrica. Todos los elementos que no tienen entre los dos en común.
text = "Diferencia simétrica."
diff_simetric = set_1.symmetric_difference(set_2)
print(text,diff_simetric)




