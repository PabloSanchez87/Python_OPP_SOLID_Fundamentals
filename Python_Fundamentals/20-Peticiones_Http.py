class colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
import os
"""
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
"""

#  * EJERCICIO:
#  * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
#  * una petición a la web que tú quieras, verifica que dicha petición
#  * fue exitosa y muestra por consola el contenido de la web.

# Métodos de petición HTTP: GET - HEAD - POST - PUT - DELETE - CONNECT - OPTIONS -TRACE - PATCH
import requests # módulo para peticiones de red.
print(f"{colors.BLUE}-{colors.RESET}"*34)

# Códigos de estado: 1XX(informativo) - 2XX(éxito) - 300(redirección) - 400(error del cliente) - 500(error del servidor)
    # 1XX - Códigos informativos: el servidor acusa recibo y está procesando la solicitud.
    # 2XX - Códigos de éxito: el servidor ha recibido, entendido y procesado correctamente la solicitud.
    # 3XX - Códigos de redirección: el servidor recibió la solicitud, pero hay una redirección a otro lugar 
    #       (o, en casos raros, debe completarse alguna acción adicional distinta de una redirección). 
    # 4XX - Códigos de error del cliente: el servidor no pudo encontrar (o alcanzar) la página o el web. Se trata de un error de web. 
    # 5XX - Códigos de error del servidor: el cliente hizo una petición válida, pero el servidor no pudo completarla. 
# print(response.text) --> Muestra por consola el contenido de la web.
response = requests.get("https://github.com/PabloSanchez87/Python_OPP_SOLID_Fundamentals")
# print(response)

# Verifica que dicha petición ha sido exitosa.

print(f"{colors.BLUE} -. Ejercicio inicial .- {colors.RESET}")
if response.status_code == 200:
    print(f"{colors.GREEN}Petición exitosa. Código: {response.status_code}{colors.RESET}")
else:
    print(f"{colors.RED}Error. Código {response.status_code}{colors.RESET}")

print(f"{colors.BLUE}-{colors.RESET}"*34)
                            ###############
                            ##   EXTRA   ##
                            ###############

#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
#  * terminal al que le puedas solicitar información de un Pokémon concreto
#  * utilizando su nombre o número.
#  * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
#  * - Muestra el nombre de su cadena de evoluciones
#  * - Muestra los juegos en los que aparece
#  * - Controla posibles errores      

print(f" {colors.BLUE}-. EXTRA .-. POKEMON .- {colors.RESET}")
print(f"{colors.BLUE}-{colors.RESET}"*34)

# Función para solicitar al usuario un nombre o número de Pokémon y convertirlo a minúsculas.
def user_input():
    return input(f"{colors.GREEN}Introduce un nombre o el número del Pokémon a buscar: {colors.RESET}").lower()

# Función para realizar una solicitud GET a una URL dada.
def get_request(url):
    response = requests.get(url)
    return response

# Función para verificar y convertir la respuesta de la solicitud a formato JSON.
def check_response_json(response):
    if response.status_code == 200:
        return response.json()
    else:
        print(f"{colors.RED}Error. {response.status_code}.{colors.RESET}")
        return None

# Función para imprimir los datos básicos de un Pokémon.
def print_pokemon_data(data):
    print("   · Nombre:", data["name"])
    print("   · ID:", data["id"])
    print("   · Peso:", data["weight"])
    print("   · Altura:", data["height"])
    types = [type["type"]["name"] for type in data["types"]]
    print("   · Tipo(s):", ", ".join(types))
    print(f"{colors.GREEN}-{colors.RESET}"*34)

# Función recursiva para imprimir los nombres en la cadena de evolución de un Pokémon.
def get_evolves(data_chain):
    print(f"   · {data_chain['species']['name']}")
    if "evolves_to" in data_chain:
        for evolve in data_chain["evolves_to"]:
            get_evolves(evolve)

# Función para obtener y mostrar la cadena de evolución de un Pokémon.
def get_evolutions(response_evolution):
    url_api_evolution_chain = response_evolution.json()["evolution_chain"]["url"]
    response_evolution_chain = get_request(url_api_evolution_chain)
    data_chain = check_response_json(response_evolution_chain)
    print(f"{colors.GREEN}Cadena de evolución: {colors.RESET}")
    get_evolves(data_chain["chain"])

# Función para obtener las versiones de juego en las que ha aparecido un Pokémon.
def get_games_versions(data):
    list_versions = []
    for game in data["game_indices"]:
        list_versions.append(game["version"]["name"])
    return list_versions

# Función para imprimir las versiones de juego en las que ha aparecido un Pokémon.
def print_versions(list_versions):
    print(f"{colors.GREEN}Versiones en las que ha aparecido:{colors.RESET}")
    print(f"{colors.GREEN}----------------------------------{colors.RESET}")
    # Iterar sobre la lista e imprimir máximo 3 elementos por línea
    count = 0
    for version in list_versions:
        if count < 2:
            print(f'  {version.capitalize()}', end=", ")
            count += 1
        else:
            print(f'  {version.capitalize()}')
            count = 0
    print()  # Imprimir una línea en blanco al final

# Función principal para obtener y mostrar los datos de un Pokémon y su cadena de evolución.
def get_pokemon():
    # Solicita al usuario el nombre o número del Pokémon.
    pokemon = user_input()
    # Construye las URLs de la API para obtener datos del Pokémon y de su cadena de evolución.
    URL_API = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    URL_API_EVOLUTION = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}"
    # Realiza la solicitud GET para obtener datos del Pokémon y verifica la respuesta.
    response = get_request(URL_API)
    data = check_response_json(response)
    if data is None: 
        return print(f"{colors.RED}No se pudieron obtener los datos del Pokémon.{colors.RESET}")
    # Imprime los datos básicos del Pokémon.
    print_pokemon_data(data)  
    # Realiza la solicitud GET para obtener datos de la cadena de evolución y verifica la respuesta.
    response_evolution = get_request(URL_API_EVOLUTION)
    data_evolution = check_response_json(response_evolution)
    if data_evolution is None:
        return print(f"{colors.RED}No se pudieron obtener las evoluciones de los datos del Pokémon.{colors.RESET}")
    # Muestra la cadena de evolución del Pokémon.
    get_evolutions(response_evolution)

    print(f"{colors.GREEN}-{colors.RESET}"*34) 

    # Obtiene las versiones de juego en las que ha aparecido el Pokémon.
    list_versions = get_games_versions(data)
    # Imprime las versiones de juego.
    if list_versions:
        print_versions(list_versions)

# Bucle principal.
def loop_execute(get_pokemon):
    while True:
        get_pokemon()
        continuar = input(f"\n{colors.GREEN}¿Quieres buscar otro Pokémon? (s/n): {colors.RESET}").lower()
        if continuar != "s":
            print(f"\n{colors.RED}¡Hasta luego!{colors.RESET}")
            break  # Sale del bucle while y termina el programa.
        print()
        os.system('clear')
 

# Llama a la función principal para comenzar el proceso.
loop_execute(get_pokemon)



                