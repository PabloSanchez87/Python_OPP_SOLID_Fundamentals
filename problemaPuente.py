"""
Problema del puente
    Tienes que cruzar un puente de noche. Sólo pueden cruzar el puente máximo 2 personas y sólo tienen 15 minutos para hacerlo.
    Siempre tiene que volver alguien por el puente para traer la linterna y poder cruzar.
    Tiempo máximo para cruzar 15 minutos.
    Protragonistas:
        Anciano = 8 minutos
        Adulto = 5 minutos
        Joven = 2 minutos
        Adolescente = 1 minutos
    Crea un programa para ir eligiendo el orden para ir a cruzar.
"""
class colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'

class InvalidIndex(Exception):
    pass

# Diccionario con los protragonistas
users = {
    "Elder" : [8, "A"], 
    "Adult" : [5, "A"],
    "Young" : [2, "A"], 
    "Teenager" : [1, "A"]
}

# Variables inicializadas.
max_time = 15 # Tiempo máximo para cruzar el puente.
side_A_validator = True # Inicializamos a True pq todos están en este lado incialmente
side_B_validator = False # Inicializamos a False pq nadie está en este lado incialmente

# Función para comprobar que lados del puente tiene gente.
def empty_side(users:dict):
    
    side_A = any("A" in data[1] for data in users.values()) # Devuelve True si encuentra alguien en el lado A
    side_B = any("B" in data[1] for data in users.values()) # Devuelve True si encuentra alguien en el lado B
    return side_A, side_B

# Mostramos la gente que hay en el lado A. Devolvemos una lista.
def show_side_A(users:dict):
    index = 1
    list_user_A = [] # Inicializamos una lista con la gente de este lado.
    print(f"\n{colors.BLUE}· Listado de gente en el lado A del puente:{colors.RESET}\n")
    for user, data in users.items():
        if "A" in data[1]:
            print(f"\t{index} - {user} --> tiempo: {data[0]} minutos")
            index += 1
            list_user_A.append((user,data))
    return list_user_A

# Mostramos la gente que hay en el lado B. Devolvemos una lista.
def show_side_B(users:dict):
    index = 1
    list_user_B = [] # Inicializamos una lista con la gente de este lado.
    print(f"\n{colors.BLUE}· Listado de gente en el lado B del puente:\n{colors.RESET}")
    for user, data in users.items():
        if "B" in data[1]:
            print(f"\t{index} - {user} --> tiempo: {data[0]} minutos")
            index += 1
            list_user_B.append((user,data))
    return list_user_B

# Función para hacer la selección de quien cruzará.
def select_side_A(side_A: list):
    print(F"{colors.BLUE}\n Seleccione con los índices quien quieres que cruce del lado A.{colors.RESET}\n")
    while True:
        try:
            user_1 = int(input("\tUsuario 1: "))
            if len(side_A) > 1:                         # Si solo queda un usuario por pasar lo controlamos
                user_2 = int(input("\tUsuario 2: "))      # y lanzamos el break.
            else:
                user_2 = 1                              # inicializamos user_2 a 1.
                break
            if user_1 == user_2:
                print(f"{colors.RED}\nERROR. No puese seleccionar a la misma persona.{colors.RESET}\n")
            elif (0 <= (user_1-1) < len(side_A)) and (0 <= (user_2-1) < len(side_A)):
                break       
            else:
                raise InvalidIndex
        except InvalidIndex:
            print(f"\n{colors.RED}ERROR. Seleccione sobre el indice indicado.{colors.RESET}\n")
        except:
            print(f"{colors.RED}\nERROR. Seleccione sobre el indice indicado.{colors.RESET}\n")
    return (user_1-1), (user_2-1)

# Función donde le pasa el diccionario y la lista generada con una lista de cada posición del diccionario seleccionada
# Con esos datos y sabiendo el indice de la lista que seleccionó el usuario, cambiamos el valor correspondiente del diccionario
# Devolvemos el valor de max_time.
def save_changes_side_A(side_A:list, users:dict, max_time:int):
    user_1, user_2 = select_side_A(side_A)

    # Aprovechando la misma lista sacamos los valores de los minutos para restarselos al tiempo máximo.
    max_time = max_time - max(users[side_A[user_1][0]][0],users[side_A[user_2][0]][0]) 

    # Cogemos la posición de la lista, y comparamos la clave almacenada en esa lista para cambiar el valor del diccionario.
    users[side_A[user_1][0]][1] = "B"
    users[side_A[user_2][0]][1] = "B"

    side_A_validator, side_B_validator = empty_side(users) # Comprobamos que lados tienen gente.

    return max_time, side_A_validator, side_B_validator

# Función para hacer la selección de quien cruzará.
def select_side_B(max_time:int ,side_B: list):
    print(f"\n· Tiempo restante para cruzar el puente: {colors.RED}{max_time} minutos.{colors.RESET}")
    print(f"\n{colors.BLUE} Seleccione el índice que quieres que cruce de vuelta del lado B.{colors.RESET}\n")
    while True:
        try:
            user_1 = int(input("\tUsuario: "))
            if (0 <= (user_1-1) < len(side_B)):
                break       
            else:
                raise InvalidIndex
        except InvalidIndex:
            print(f"\n{colors.RED}ERROR. Seleccione sobre el indice indicado.{colors.RESET}\n")
        except:
            print(f"\n{colors.RED}ERROR. Seleccione sobre el indice indicado.{colors.RESET}\n")
    return (user_1-1)

# Función donde le pasa el diccionario y la lista generada con una lista de cada posición del diccionario seleccionada
# Con esos datos y sabiendo el indice de la lista que seleccionó el usuario, cambiamos el valor correspondiente del diccionario
# Devolvemos el valor de max_time.
def save_changes_side_B(side_B:list, users:dict, max_time:int):
    user_1 = select_side_B(max_time, side_B)

    # Aprovechando la misma lista sacamos los valores de los minutos para restarselos al tiempo máximo.
    max_time = max_time - users[side_B[user_1][0]][0]

    # Cogemos la posición de la lista, y comparamos la clave almacenada en esa lista para cambiar el valor del diccionario.
    users[side_B[user_1][0]][1] = "A"

    side_A_validator, side_B_validator = empty_side(users) # Comprobamos que lados tienen gente.

    return max_time, side_A_validator, side_B_validator


# Funcion main
def main(max_time):

    side_A = []
    side_B = []

    print(f"{colors.BLUE}\n\t ***************************")
    print("\t *   PROBLEMA DEL PUENTE   *")
    print(f"\t ***************************{colors.RESET}")

    while max_time > 0:
        side_A_validator, side_B_validator = empty_side(users) # Comprobamos que lados tienen gente.

        print(f"\n· Tiempo restante para cruzar el puente: {colors.RED}{max_time} minutos.{colors.RESET}") # Mostramos el tiempo que nos queda para cruzar

        if side_A_validator: # Si encuentra gente en el lado A, imprime listado.
            side_A = show_side_A(users) # Mostramos el listado de la gente en el lado A.
        if side_B_validator: # Si encuentra gente en el lado B, imprime listado.
            side_B = show_side_B(users) # Mostramos el listado de la gente en el lado B.

        max_time, side_A_validator, side_B_validator = save_changes_side_A(side_A, users, max_time)

        if side_B_validator and max_time > 0:
            side_A = show_side_A(users) # Mostramos el listado de la gente en el lado A.
            side_B = show_side_B(users) # Mostramos el listado de la gente en el lado B.
            max_time, side_A_validator, side_B_validator = save_changes_side_B(side_B, users, max_time)

        if not side_A_validator and max_time >=0:
            print(f"\n{colors.GREEN}GENIAL!! Lo has conseguido! ESTÁIS A SALVO!!!!{colors.RESET}\n")
            break
    
    else:
        print(f"\n{colors.RED}GAME OVER. Se ha acabado el tiempo sin que todos hayan cruzado.{colors.RESET}\n")
        print(f"\t{colors.RED}· Tiempo agotado!!!! {colors.RESET}\n")


main(max_time)