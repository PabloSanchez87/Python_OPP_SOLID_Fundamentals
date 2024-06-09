'''
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
'''
# Callback ---> Función que se le pasa como argumento a otra función y se espera que
#               la función de callback se ejecute en algún momento dentro de la función contenedora.
#               Se utilizan sobre todo en programación asíncrona.
#          + Ventajas: Modularidad, Reutilización, Flexibilidad.
#          + Desventajas: Mayor complidad, difícil depuración.

#  * EJERCICIO:
#  * Explora el concepto de callback en tu lenguaje creando un ejemplo
#  * simple (a tu elección) que muestre su funcionamiento.

def greeting_process(name: str, callback):
    print("Ejecutando el proceso de saludo...")
    callback(name)

def greet_callback(name:str):
    print(f"Hola, {name}!")

greeting_process("Pablo",greet_callback)


                            ###############
                            ##   EXTRA   ##
                            ###############


#  * DIFICULTAD EXTRA (opcional):
#  * Crea un simulador de pedidos de un restaurante utilizando callbacks.
#  * Estará formado por una función que procesa pedidos.
#  * Debe aceptar el nombre del plato, una callback de confirmación, una
#  * de listo y otra de entrega.
#  * - Debe imprimir un confirmación cuando empiece el procesamiento.
#  * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
#  *   procesos.
#  * - Debe invocar a cada callback siguiendo un orden de procesado.
#  * - Debe notificar que el plato está listo o ha sido entregado.

from Python_Fundamentals.Contantes import colors
import random
import time
import threading

def order_process(dish_name: str, confirm_callback, ready_callback, delivered_callback):
    """
    Inicia el proceso de un pedido en un hilo separado.
        :param dish_name: Nombre del plato.
        :param confirm_callback: Función de callback para confirmar el pedido.
        :param ready_callback: Función de callback para indicar que el pedido está listo.
        :param delivered_callback: Función de callback para indicar que el pedido ha sido entregado.
    """
    # Crea un nuevo hilo para ejecutar la función `process`.
    threading.Thread(
        # Especifica la función `process` como el objetivo a ejecutar en el hilo.
        target=process, 
        # Pasa los argumentos necesarios para la función `process`.
        args=(dish_name, confirm_callback, ready_callback, delivered_callback)
    ).start()  # Inicia el hilo.

def process(dish_name: str, confirm_callback, ready_callback, delivered_callback):
    """
    Procesa el pedido siguiendo los pasos de confirmación, preparación y entrega,
    e invoca las funciones de callback correspondientes.
        :param dish_name: Nombre del plato.
        :param confirm_callback: Función de callback para confirmar el pedido.
        :param ready_callback: Función de callback para indicar que el pedido está listo.
        :param delivered_callback: Función de callback para indicar que el pedido ha sido entregado.
    """
    # Llamada a la función de callback para confirmar el pedido
    confirm_callback(dish_name)
    # Simulación del tiempo de espera para la preparación del pedido
    wait_time = random.randint(1, 30)
    print(f"{colors.RED}Tiempo de espera preparación: {wait_time} seg. de la orden de {dish_name}{colors.RESET}")
    time.sleep(wait_time)
    # Llamada a la función de callback para indicar que el pedido está listo
    ready_callback(dish_name)
    # Simulación del tiempo de espera para la entrega del pedido
    wait_time = random.randint(1, 10)
    print(f"{colors.RED}Tiempo de espera para entrega: {wait_time} seg. de la orden de {dish_name}{colors.RESET}")
    time.sleep(wait_time)
    # Llamada a la función de callback para indicar que el pedido ha sido entregado
    delivered_callback(dish_name)

def confirm_order(dish_name: str):
    """
    Imprime un mensaje confirmando que el pedido ha sido recibido.
        :param dish_name: Nombre del plato.
    """
    print(f"{colors.YELLOW} · Tu pedido {dish_name} ha sido confirmado.{colors.RESET}")

def order_ready(dish_name: str):
    """
    Imprime un mensaje indicando que el pedido está listo.
        :param dish_name: Nombre del plato.
    """
    print(f"{colors.BLUE} · Tu pedido {dish_name} ha sido preparado.{colors.RESET}")

def order_delivered(dish_name: str):
    """
    Imprime un mensaje indicando que el pedido ha sido entregado.
        :param dish_name: Nombre del plato.
    """
    print(f"{colors.GREEN} · Tu pedido {dish_name} ha sido entregado.{colors.RESET}")

# Simulación de pedidos
order_process("Pizza 4 Quesos", confirm_order, order_ready, order_delivered)
order_process("Pizza Margarita", confirm_order, order_ready, order_delivered)
order_process("Pizza Barbacoa", confirm_order, order_ready, order_delivered)
order_process("Pizza Fantasía", confirm_order, order_ready, order_delivered)
order_process("Pizza Carbonara", confirm_order, order_ready, order_delivered)


