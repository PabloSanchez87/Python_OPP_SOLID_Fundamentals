"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""
### CADENA DE CARACTERES.
# Operaciones

s1 = "Hola"
s2 = "Python"
s3 = "Pablo Sanchez @sanchezdev"

# Concatenación
print(f"{s1} {s2}")

# Repetición
print(f"{s1} "*3)

# Indexación
print(s1[1])
print(s1[3])

# Longitud
print(len(s1))

#Slicing (porción)
print(s2[2:5])
print(s2[2:])
print(s2[:2])

# Búsqueda
print("a" in s1)
print("c" in s1)

# Reemplazo
print(s1.replace("o", "a"))

# División
print(s2.split("t")) # Desechamos el punto por donde cortamos.

# Conversión mayúsculas o minúsculas
print(s1.upper())
print(s1.lower())
title = "pablo sanchez"
print(title.title())
print(title.capitalize())

# Eliminiación de espacios al principio y al final
print(" pablo sanchez ".strip()) # Eliminamos los espacios en blanco al principio y final.

# Busqueda al principio.
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("hon"))

# Busqueda de posición
print("Pablo Sanchez @sanchezdev".find("sanchez"))
print("Pablo Sanchez @sanchezdev".find("Sanchez"))
print("Pablo Sanchez @sanchezdev".find("S"))
print("Pablo Sanchez @sanchezdev".lower().find("s"))

# Busqueda de ocurrencias
print(s3.lower().count("s"))

# Interpolación
print(f"Saludo: {s1}, lenguaje: {s2}!")

# Formateo
print("Saludo: {}, lenguaje: {}!".format(s1, s2))

# Transformación en un lista de caracteres.
print(list(s3))

# Transformación de una lista en una cadena
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

# Transformaciones numñericas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Comprobaciones varias.
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())

### EXTRA ###
def check(w1:str, w2:str):
    # Palindromos
    print(f"¿{w1} es un palíndromo?: {w1 == w1[::-1]}")
    print(f"¿{w2} es un palíndromo?: {w2 == w2[::-1]}")

    # Anagramas -->  Contienen las mismas letras.
    print(f"¿{w1} es un anagrama?: {sorted(w1) == sorted(w2)}")

    # Isogramas --> Cada letra aparece el mismo número de veces.
    print(len(w2))
    print(len(set(w2)))

    # Creo un diccionario con letras y cantidad de veces que aparece.
    word_dict = dict()
    for word in w2:
        word_dict[word] = word_dict.get(word, 0) +1

    # Compruebo con un bucle si es un isograma.
    isogram = True
    values =  list(word_dict.values())
    isogram_len = values[0]
    for word_count in values:
        if word_count != isogram_len:
            isogram = False
            break
    
    print(isogram)
    print(word_dict)
    
    print(f"¿{w2} es un isograma?: {isogram == True}")


check("radar", "python")
#check("amor", "roma")

