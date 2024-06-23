# PATRONES DE DISEÑO: DECORADORES
""" 
* Explora el concepto de "decorador" y muestra cómo crearlo
* con un ejemplo genérico.
*
* DIFICULTAD EXTRA (opcional):
* Crea un decorador que sea capaz de contabilizar cuántas veces
* se ha llamado a una función y aplícalo a una función de tu elección.
"""
""" DEFINICIÓN 
Es una función que se utiliza para extender o modificar la funcionalidad
de esa función, pero sin modificar la función.
"""
                            ###############
                            ## EJERCICIO ##
                            ############### 
# * Explora el concepto de "decorador" y muestra cómo crearlo
# * con un ejemplo genérico.

# Función decoradora.
def print_call(function):
    def print_function(): # Wrapper
        print(f"La función {function.__name__} ha sido llamada.")
        return function
    return print_function


@print_call
def example_function():
    pass


@print_call
def example_function_2():
    pass


@print_call
def example_function_3():
    pass


example_function()
example_function_2()
example_function_3()

print("·"*50)
                            ###############
                            ##   EXTRA   ##
                            ###############
# * DIFICULTAD EXTRA (opcional):
# * Crea un decorador que sea capaz de contabilizar cuántas veces
# * se ha llamado a una función y aplícalo a una función de tu elección.

def call_counter(function):
    def counter_function():
        counter_function.call_count += 1
        print(f"La función {function.__name__} se ha llamado {counter_function.call_count} vez(es).") 
        return function
    
    counter_function.call_count = 0   
    return counter_function


@call_counter
def example_function_4():
    pass


@call_counter
def example_function_5():
    pass


example_function_4()
example_function_5()
example_function_4()
example_function_5()
example_function_5()
example_function_5()
example_function_4()

# Existe una instancia para cada función que ha sido llamada. Por eso a pesar
# de usar el mismo decorador en las dos funciones, las variables de la instancia 
# son únicas. Por esta razón, al llamar al decorador en las distintas funciones 
# obtenemos resultados diferentes (o el que corresponda según el estado de cada función).