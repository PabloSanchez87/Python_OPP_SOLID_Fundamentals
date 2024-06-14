"""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
# Slide
chain_str = "Hola mundo"
print(chain_str[::-1])

# Bucle
def reverse_chain(chain_str):
    reverse_chain_str = ""
    for i in chain_str:
        reverse_chain_str = i + reverse_chain_str
    return f"{reverse_chain_str}"
print(reverse_chain(chain_str))

# Función reverse.
list_chain = list(chain_str)
list_chain.reverse()
reverse_chain_str = "".join(list_chain)
print(reverse_chain_str)


