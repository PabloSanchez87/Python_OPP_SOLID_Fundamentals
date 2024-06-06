"""
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 """
# Estándar para analizar cadenas de texto, buscar algo, validar,...

# importamos la librería de expresiones regulares
import re
import unittest # importamos unittest

# Texto a buscar.
text = "Este es el ejercicio 16 publicado el 15/04/2024."

# Función para buscar en el texto con una expresión regular.
def find_numbers(text:str) -> list:
    # En caso de python debe empezar por "r" la expresión regular.
    # EXPRESIÓN REGULAR.
    #   regex = r"[0-9]+" 
    regex = r"\d+"
    
    # Devolvemos el resultado.
    return re.findall(regex, text)

# Llamada a la función e imprimimos.
print(find_numbers(text))


                #############
                ### EXTRA ###
                #############

 # Crea 3 expresiones regulares capaces de:
    # - Validar un email.
def validate_email(email:str) -> bool:
    """
    ^ -->                 indica inicio cadena
    [a-zA-Z0-9._%+-]+ --> puede contener letras mayúsculas y minúsculas, números, los caracteres indicados 
                            y el + indica que deben aparecer al menos una vez.
    @ -->                 debe aparecer el arroba.
    [a-zA-Z0-9.-]+ -->    nombre dominio, puede contener letras mayúsculas y minúsculas, números, guión y "." 
                            y el + indica que debe aparecer al menos una vez.
    \. -->                Un punto literal, que sepera el dominio de la extensión del dominio.
    [a-zA-Z]{2,} -->      Extensión del dominio, debe contener al menos 2 letras mayúscylas o minúsculas y
                            deben aparecer al menos 2 veces {2,}
    $ -->                 indica el final de la cadena
    """
    return bool(re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email))

print("Comprobamos emails:")
print(validate_email("sancheztorrespablo@gmail.com"))       # true
print(validate_email("Sanchez-t0rres^Pablo@gmail..com"))    # false
print(validate_email("Sanchez-t0rresPablo87@gm-ail.com"))   # true
print(validate_email("Sanchez-t0rresPablo87@gm_ail.com"))   # false


    # - Validar un número de teléfono.

def validate_phone(phone:str) ->bool:  # Restringimos a teléfono español.

    """
    ^ -->                         indica inicio cadena
    (?:\+?34)? -->                permite que el número empiece con un código del país opcional +34, donde ? indica
                                    que puede aparecer 0 o 1 vez, y (? ...) es un grupo de no captura.
    (?:[67]\d{1}|[89]\d{1})-->    Grupo de no captura, chequea los primeros dígitos del número. Puede empezar por 6 o 7,
                                    seguido de cualquier dígito \d{1} o un número que empieza con 8 o 9. (parte expresión según móvil o fijo.)
    \d{7} -->                     Captura los últimos 7 dígitos del número.
    $ -->                         indica el final de la cadena
    """
    return bool(re.match(r"^(?:\+?34)?(?:[67]\d{1}|7[1-9]\d{1})\d{7}$", phone)) or bool(re.match(r"^(?:\+?34)?(?:6\d{1}|[89]\d{1})\d{7}$", phone)) 

print("Comprobamos teléfonos:")
print(validate_phone("981535353"))      # True
print(validate_phone("9815O5e53"))      # False
print(validate_phone("98153535"))       # False
print(validate_phone("281535353"))      # False
print(validate_phone("+34636922888"))   # True
print(validate_phone("34636922888"))    # True
print(validate_phone("+34636922e88"))   # False 
print(validate_phone("+34736922888"))   # True
print(validate_phone("+34636922"))      # False
print(validate_phone("+346369228888"))  # False


    # - Validar una url.

def validate_url(url:str) -> bool:

    return bool(re.match(r"^(http[s]?)?(://)?(www.)?[\w]+\.[a-zA-Z0-9]+$", url))
        # Nota:  Habría que adaptar la url a las condiciones exactas de url que queremos controlar.


print("Comprobamos URLs:")
print(validate_url("https://www.example.com"))                                      # True
print(validate_url("http://www.example.com"))                                       # True
print(validate_url("ftp://example.com"))                                            # False
print(validate_url("www.example.com"))                                              # True
print(validate_url("example.com"))                                                  # True
print(validate_url("http://example.com/page1"))                                     # False


# Anexo:

def validate_url_VSCode(url:str) -> bool:
    # Expresión regular usada en VSCode para identificar urls. Expresión básica.
    return bool(re.match(r"(https?|ftp)://[-a-zA-Z0-9@:%._\+~#?&//=]*", url))

print("Comprobamos URLs con ER de VSCode:")
print(validate_url_VSCode("https://www.example.com"))                                      # True
print(validate_url_VSCode("http://www.example.com"))                                       # True
print(validate_url_VSCode("ftp://example.com"))                                            # True
print(validate_url_VSCode("www.example.com"))                                              # False
print(validate_url_VSCode("example.com"))                                                  # False
print(validate_url_VSCode("http://example.com/page1"))                                     # True
