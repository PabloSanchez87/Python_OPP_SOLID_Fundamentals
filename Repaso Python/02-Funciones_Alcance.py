"""
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

### FUNCIONES

# FUNCIONES DEFINIDAS POR EL USUARIO
# Simples.
def greet():
    print("Hola, Python!")

greet()

# Con retorno.
def return_greet():
    return "Hola, Python!"


print(return_greet())

# Con argumento.
def arg_greet(name):
    print(f"Hola, {name}!")

arg_greet("Pablo")

# Con argumentos.
def args_greet(greet,name):
    print(f"{greet}, {name}!")

args_greet("Hola", "Pablo")
args_greet( name="Pablo",greet="Hola")

# Con argumento por defecto.
def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")

default_arg_greet()
default_arg_greet("Pablo")

#Con argumentos y retorno.
def rerturn_args_greet(greet,name):
    return f"{greet}, {name}!"

print(rerturn_args_greet("Hola", "Pablo"))

# Con return de varios valores
def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Con número variable de argumentos.
def variable_arg_greet(*names): # Podemos pasarle más de un valor.
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Pablo", "Sanchez")

# Con número variable de argumentos con palabra clave.
def variable_arg_greet_key(**names):
    for key, name in names.items():
        print(f"{name} ({key})!")

variable_arg_greet_key(
    language="Python", 
    name="Pablo", 
    apellido = "Sanchez",
    edad=36
    )

## FUNCIONES PARA DENTRO DE FUNCIONES
def outer_function():
    def inner_function():
        print("Funcion interna.")
    inner_function()

outer_function()

## FUNCIONES DEL LENGUAJE (BUILT-IN)
print(len("PabloDev"))
print(type("PabloDev"))
print("PabloDev".upper())

## SCOPE LOCAL Y GLOBAL
global_var = "Python"
print(global_var)

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}")
hello_python()
#print(local_var) no se puede acceder fuera de la function

#### EXTRA #####

def print_numbers(t1, t2) -> int: ## ejercicio jizzbuzz
    count = 0
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(t1 + t2)
        elif number % 3 == 0:
            print(t1)
        elif number % 5 == 0:
            print(t2)
        else:
            print(number)
            count += 1
    return count

print(print_numbers("Fizz", "Buzz"))





