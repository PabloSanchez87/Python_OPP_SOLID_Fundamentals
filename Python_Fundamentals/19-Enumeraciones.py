"""
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
 """

#  * EJERCICIO:
#  * Empleando tu lenguaje, explora la definición del tipo de dato
#  * que sirva para definir enumeraciones (Enum).
#  * Crea un Enum que represente los días de la semana del lunes
#  * al domingo, en ese orden. Con ese enumerado, crea una operación
#  * que muestre el nombre del día de la semana dependiendo del número entero
#  * utilizado (del 1 al 7).

## Enum:  Conjuntos de CONSTANTES nombradas.
##        Ayuda a delimitar cuales son los valores con los que podemos trabajar.

from enum import Enum

# Tenemos que crear una clase para crear un enum. Creamos un tipo de dato acotado. Más seguro, más rápido, más legible.
class Weekday(Enum):   # Hereda del comportamiento de Enum
    MONDAY = 1
    TUESDAY = 2
    WENDESDAY = 3
    THURDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Función que muestre el nombre del día de la semana dependiendo del número entero
#  * utilizado (del 1 al 7)
def get_day(number : int):
    print(Weekday(number).name)

# Imprimimos el valor del enum según el valor dado.
for number in range(1,8):
    get_day(number)


                    ###############
                    ##   EXTRA   ##
                    ###############

#  * DIFICULTAD EXTRA (opcional):
#  * Crea un pequeño sistema de gestión del estado de pedidos.
#  * Implementa una clase que defina un pedido con las siguientes características:
#  * - El pedido tiene un identificador y un estado.
#  * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
#  * - Implementa las funciones que sirvan para modificar el estado:
#  *   - Pedido enviado
#  *   - Pedido cancelado
#  *   - Pedido entregado
#  *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
#  * - Implementa una función para mostrar un texto descriptivo según el estado actual.
#  * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 

class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4

class Order:

    def __init__(self, id:int, status=OrderStatus.PENDING) -> None:
        self.id = id
        self.status = status

    def ship(self):
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.SHIPPED
            self.display_status()
        else:
            print("El pedido ya ha sido enviado o cancelado.")

    def deliver(self):
        if self.status == OrderStatus.SHIPPED:
            self.status = OrderStatus.DELIVERED
            self.display_status()
        else:
            print("El pedido necesita ser enviado antes de entregarse.")

    def cancel(self):
        if self.status == OrderStatus.DELIVERED:
            self.status = OrderStatus.CANCELLED
            self.display_status()
        else:
            print("El pedido ya ha sido entregado o no ha sido enviado.")

    def display_status(self):
        print(f"El estado del pedido {self.id} es {self.status.name}")


order_1 = Order(1)
order_1.deliver()
order_1.ship()
order_1.deliver()
order_1.cancel()

order_2 = Order(2, OrderStatus.SHIPPED)
