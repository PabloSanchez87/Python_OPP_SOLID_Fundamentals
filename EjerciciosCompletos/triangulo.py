'''
EL TRIÁNGULO:
En una obra es necesario construir para el tejado de una casa una estructura triangular con tres 
piezas. El ingeniero se pregunta si dadas la largura de las piezas que ha recibido podrá construir 
este estructura. Crea un script que dados tres longitudes indique si podría construirse un triangulo 
con esas piezas.
(Pista: la suma de dos piezas tiene que ser mayor que el lado restante. Esto debe ser así para 
todas las posibles combinaciones)
'''


from termcolor import colored                                                               ## ITERTOOLS IMPORT COMBINTIONS
from itertools import combinations                                                          ## --> combinations(lista, tamaño_combinación) gerera todas las posibles
                                                                                            ##          cadenas de una lista del tamaño indicado.
lista_Longtudes = []
print(colored("\nINTRODUZCA LAS 3 LONGITUDES). \n", "grey")) 

def lectura_Lados():                                                                        # Devolvemos la lista de números.
    while len(lista_Longtudes)!=3:
        try:
            largo = float(input("Introduzca un número: "))      
            if isinstance(largo,float):                                                     # Controla que largo sea del tipo flotante.
                lista_Longtudes.append(largo)                                               # Encadena en la lista el número introducido.
        except:
            print(colored("\n\tError. Dato incorrecto.\n", "red"))
    print()
    return lista_Longtudes


def control_Longitudes(lista_Longitudes):                                                   # Controlamos las combinaciones de las longitudes obtenidas.
    contador = 0                                                                            # Inicializamos el contador que devolverá la función.
    for sumaDosLados in combinations(lista_Longitudes,2):                                   # Con el for recorremos todas las combinaciones que nos presenta de tamaño 2 la funcion combinations.
        if sum(sumaDosLados) > max(lista_Longitudes):                                       # Sum nos devuelve la suma de la lista que le indicamos, en este caso la suma de la combinación iterada.
            print(sumaDosLados, "=", sum(sumaDosLados), "-->",  max(lista_Longitudes))      # Max nos devuelve el valor maximo de la lista que le indicamos.
            contador = contador + 1                                                         # Si la suma de la interación es mayor que el valor máximo de la lista, 
                                                                                            # sumamos uno al contador.
        else:
            print(sumaDosLados, "=", sum(sumaDosLados), "-->",  max(lista_Longitudes))      # En caso contrario, no aumentamos el contador.
    return contador                                                                         # Devolvemos el valor del contador, para que se pueda formar el triángulo debe 
                                                                                            # valer 3.


# Algoritmo principal.
lista_Longitudes = lectura_Lados()                                                          # Pedimos los datos con la funcion lectura_lados.
contador = control_Longitudes(lista_Longitudes)                                             # Ejecutamos la funcion control_longitudes y almacenamos el valor del contador.
if contador == 3:                                                                           # Si el contador es igual a 3, se puede formar el triángulo.
    print(colored("\nSe puede formar un triángulo con las 3 longitudes.\n", "green"))       
else:                                                                                       # Si el contador no es 3, no se puede formar el triángulo.
    print(colored("\nNo se puede formar un triángulo con las 3 longitudes.\n", "red"))
