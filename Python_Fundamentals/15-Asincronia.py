"""
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
 """

### ASINCRONÍA
import datetime
import time
import asyncio # librería de asincronía

async def task (name: str, duration: int): # indicamos async
    print(f"Tarea: {name}. Duration: {duration}s. Inicio: {datetime.datetime.now()} ")
    await asyncio.sleep(duration) 
    print(f"Tarea: {name}. Fin: {datetime.datetime.now()}")

asyncio.run(task("1", 1)) # usamos asyncio.run para correr la tarea asincrona.

### EXTRA ###
# Para lanzar las funciones en paralelo. Pero tenemos que indicar el await
# Definimos un contexto asincrono para poder lanzar el await despues.
# PAra que no falle tenemos que usar un asyncio.sleep() en vez del time.sleep (este ultimo entorpece la ejecución)
# pero tenemos que indicarle el await para que espere. (tanto en el sleep como en la funcion async_tasks)
async def async_tasks():
    await asyncio.gather(task("C", 3), task("B", 6), task("A", 5))
    
    await task("D", 1)   #Espera a que acaben la anteriores antes de empezar. Debemos poner el await para que se espere su ejecución.

asyncio.run(async_tasks())
