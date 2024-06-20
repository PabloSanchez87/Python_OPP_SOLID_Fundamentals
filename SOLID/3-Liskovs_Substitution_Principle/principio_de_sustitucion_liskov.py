## SOLID
# Single Responsability PRinciple
# Open/Closed Principle
# Liskov's Substitution Principle
# Interface Segregation
# Dependency  Inversion
"""
Conjunto de reglas y mejores prácticas a seguir al diseñar
una estructura de clase.

Autor: Robert J. Martin

Sirven para crear un código comprensible, legible y comprobable
en el que muchos desarrolladores pueden trabajar en colaboración.
"""
# Liskov's Substitution Principle
""" 
Definición: Si S es un subtipo de T, entonces los objetos de tipo T
en un programa pueden ser reemplazados por objetos del tipo S sin
alterar ninguna de las propiedades deseables del programa (correctitud,
tarea realizada, ...)
Beneficios:
    - Reutilización del código
    - Mantenimiento del código
    - Polimosfirmo
    - Correctitud (NO NECESITAMOS CORREGIR CÓDIGO)
"""
"""
 ---> EJEMPLO:
Vehicle{
    getSpeed
    getCubicCapacity
}
Car(Vehicle){
    getSpeed
    getCubicCapacity
    ishatchBack
}
Bus(Vehicle){
    getSpeed
    getCubicCapacity
    getEmergencyExitLoc
}

 ---> Using Liskov
vehicle Vehiculo = new Bus()
vehicle.getSpeed
vehicle = new Car
vehicle.getCubicCapacoty
"""
## NOTA. Entra ligeramente en conflicto con la herencia.
# Por ejemplo. clase persona tiene método pagar(). 
# Niño hereda de persona, pero no debería poder pagar(), pero
# necesitaría implementar el método.
# Necesitariamos clase persona, niño hereda, pero tmb hereda 
# una clase adulto. 
# En resumen, no es suficiente con saber si la clase hija ES 
# de la clase padre.

# Ejemplo de uso, comentado y refactorizado.

""""""
# Antes MetodoPago, ahora MetodoPagoBase
class MetodoPagoBase:
    def procesar_pago():
        pass
""""""

"""""" # Método creado en la refactorización.
class MetodoPagoAutomatico(MetodoPagoBase):
    def procesar_pago(self, cantidad):
        pass
""""""

"""""" # Método creado en la refactorización.
class MetodoPagoManual(MetodoPagoBase):
    def procesar_pago(self, cantidad):
        pass
""""""


## Métodos de pago automáticos   
class PagoConTarjeta(MetodoPagoAutomatico):
    def __init__(self, numero_tarjeta) -> None:
        self.numero_tarjeta = numero_tarjeta
        
    def procesar_pago(self, cantidad):
        print(f"Procesando pago automático de {cantidad} " 
              f"usando la tarjeta {self.numero_tarjeta}"
              )
        
class PagoPayPal(MetodoPagoAutomatico):
    def __init__(self, cuenta_paypal) -> None:
        self.cuenta_paypal = cuenta_paypal
        
    def procesar_pago(self, cantidad):
        print(f"Procesando pago automático de {cantidad} " 
              f"usando la cuenta {self.cuenta_paypal}"
              )

class PagoBitcoin(MetodoPagoAutomatico):
    def __init__(self, direccion_btc) -> None:
        self.direccion_btc = direccion_btc
        
    def procesar_pago(self, cantidad):
        print(f"Procesando pago automático de {cantidad} "
              f"usando la direccion {self.direccion_btc}"
              )


## Método de pago manual.
class PagoCheque(MetodoPagoManual):
    def __init__(self, numero_cheque) -> None:
        self.numero_cheque = numero_cheque
    
    """"""
    def procesar_pago(self, cantidad):
        print(f"Procesando pago manual de {cantidad} " 
              f"usando el ceque {self.numero_cheque}"
             )
    """"""
       
    # Nuestra clase hija no puede implementar todos los métodos de la clase padre
    # y no debería ser así.    
    #def procesar_pago(self, cantidad):
    #    raise NotImplementedError(
    #       "Los pagos con cheque no pueden ser procesados automáticamente."
    #       )

    #def procesar_cheque(self, cantidad):
    #    print(f"Procesando pago de {cantidad}" 
    #          f"usando el ceque {self.numero_cheque}"
    #          )

"""""" # Creamos dos métodos que implementan dos clases distintas en sus atributos
def realizar_pago_automatico(metodo_pago: MetodoPagoAutomatico, cantidad):
    metodo_pago.procesar_pago(cantidad)
    
def realizar_pago_manual(metodo_pago: MetodoPagoManual, cantidad):
    metodo_pago.procesar_pago(cantidad)
""""""

# Instanciamos clases.
pago_tarjeta = PagoConTarjeta("123 456 789")
pago_paypal = PagoPayPal("cuenta@paypal.com")
pago_btc = PagoBitcoin("fGthsdewrqeQET43")
pago_cheque = PagoCheque("987654321")

realizar_pago_automatico(pago_btc, 4000)
realizar_pago_automatico(pago_paypal, 1000)
realizar_pago_automatico(pago_tarjeta, 500)

realizar_pago_manual(pago_cheque, 1500)

# Nuestra clase hija PagoCheque no puede implementar todos los métodos de la 
# clase padre y no debería ser así.
#try:
#    realizar_pago(pago_cheque, 1500)
#except NotImplementedError as e:
#    print(e)

""""""
## Nota explicatiba.
# Teníamos un sólo método de pago, que generalizaba para todo, pero uno de sus 
# hijos no podía ser reemplazo de su padre, pq no lo hacía de forma automática. 
# Nos creamos# otra clase para el pago automático y manual que ambas heredan del 
# método de pago base.
""""""






















