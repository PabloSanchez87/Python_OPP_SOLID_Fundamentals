# Logger con Tiempo de Ejecución
"""
Imagina que estás desarrollando un sistema complejo que incluye múltiples
funciones críticas. 
Para asegurarte de que todo funcione correctamente y para realizar un 
seguimiento del tiempo de ejecución de estas funciones, decides implementar 
un decorador de registro (logger) con tiempo de ejecución.

El decorador debería realizar las siguientes acciones:
    1. Antes de llamar a la función original (puedes incluir cualquier función),
        debe imprimir un mensaje indicando que la función está a punto de
        ejecutarse.
    2. Después de que la función se haya ejecutado, debe imprimir un mensaje
        que incluya el tiempo que tardó la función en ejecutarse.
    3. Si la función original arroja una excepción, el decorador debe manejarla
        e imprimir un mensaje adecuado, indicando que se ha producido una 
        excepción.
"""

## Decoradores
# Permite modificar o extender el comportamiento de funciones o clases sin cambiar 
#   su código subyacente. Los decoradores son funciones que toman otra función (o método)
#   como argumento y devuelven una función modificada o extendida.

## Estructura de un Decorador
# Un decorador típico se define utilizando la siguiente estructura:
#   def decorador(funcion):
#       def wrapper(*args, **kwargs):
#            # Código antes de llamar a la función
#            resultado = funcion(*args, **kwargs)
#            # Código después de llamar a la función
#            return resultado
#       return wrapper

#   decorador: Es la función que actúa como decorador. 
#               Toma como parámetro la función que se va a decorar (funcion) y 
#               devuelve una función wrapper que envuelve y modifica el comportamiento 
#               de funcion.
#   wrapper: Es la función interna que se define dentro del decorador. Es responsable de
#               ejecutar código antes y/o después de llamar a la función original (funcion).

## Uso de Decoradores:
#   Agregar funcionalidad a funciones existentes: Por ejemplo, loguear información antes y 
#           después de llamar a una función, medir el tiempo de ejecución, validar parámetros, etc.

#   Modificar el comportamiento de funciones: Como cambiar el valor de retorno, cachear resultados 
#           para mejorar la eficiencia, transformar datos de entrada o salida, entre otros.

import time


def logger_tiempo_ejecucion(function):
    def wrapper():
        #Imprimimos el tiempo de ejecución.
        inicio=time.time()
        print(f"Invocando a la función '{function.__name__}' ...")
        try:
            resultado = function()
        except Exception as e:
            print(f"Se produj un error en la función '{function.__name__}': {e}")
            raise
        #Imprimimos el tiempo final de ejecución
        fin = time.time()
        tiempo_ejecucion = (fin - inicio) * 1_000_000
        print(f"La función '{function.__name__}' ha tardado {tiempo_ejecucion:.5f} microsegundo(s) en ejecutarse.")

        
        return resultado
    return wrapper
        
    
    
@logger_tiempo_ejecucion
def fibo():
    fib_series=[0,1]
    for i in range(2,20):
        fib_series.append(fib_series[i-1]+fib_series[i-2])
    return fib_series

print(fibo())