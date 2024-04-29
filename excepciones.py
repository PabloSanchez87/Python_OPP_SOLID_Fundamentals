"""
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
"""

## EXCEPCIONES
try:
    print(10/2)
    print(10/0)
except:
    print(f"No se puede dividir entre 0.")

print("Hemos llegado hasta aquí. 1 .")


try:
    my_list = [1,2,3,4]
    print(my_list[4])
except Exception as e:
    print(f"Error: {e} ({type(e).__name__})")

print("Hemos llegado hasta aquí. 2 .")

### EXTRA ###
class StrTypeError(Exception):
    pass

def process_params (params: list):
    if len(params) < 3:
        raise IndexError()
    elif params[1] == 0:
        raise ZeroDivisionError()
    elif type(params[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser una cadena de texto.")


    print(params[3])
    print(params[0]/params[1])
    print(params[2] + 5)

try:
    process_params([1,2,4,3])
except IndexError as e:
    print("El número de la lista debe ser mayor que dos.")
except ZeroDivisionError as e:
    print("No se puede dividir entre 0.")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Error inesperado: {e}")
else: ## Opcional, se imprime si no hay ningún error contemplado.
    print("No se ha producido ningún error.")
finally: ## Si o si se ejecuta el finally.
    print("Programa finalizado.")


