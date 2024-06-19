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
# Open/Closed Principle
""" 
Un artefacto (clase, método,...) de software debe estar abierto 
a ampliaciones pero cerrado a modificaciones.
    - Facilita el mantenimiento y la evolución del código a
        largo plazo
    - Mejora la modularidad y la reutilización del código
    - Reduce el riesgo de introducir errores al moficiar el
        código existente.
    - Promueve un diseño más flexible y extensible.
"""
# Ejemplo mala estructura.
""" Herencia
        Vehículo
Vehículo        Barcos
ruedas
"""
""" Polimosfismo
              Figura
             dibujar()
Triángulo    Círculo     Rectángulo
dibujar()    dibujar()    dibujar()
"""
"""  Composición
Page --> has-A --> Book
"""
""" 
class Shape
    __init__
    calculate_area()
            --> Si quisieramos añadir otro polígono tendríamos que modificar.
"""
# Ejemplo estructura Open/closed
"""
class Shape(ABC)
    __init__
    calculate_area() --> abstractmethod

class Circle(Shape)

class Rectangle(Shape)

class Square(Shape)

...                     --> Ampliamos, pero no modificamos.

"""
## Nota. Uso de métodos abstractos.
    # Algoritmos de clasificación.
    # Algoritmos de enrutamiento.


# Código no refactorizado.
print("·"*35)
print(" ·· No refactorizado ..")
class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre

    def realizar_pedido(self, tipo_pedido, detalles):
        if tipo_pedido == "para_llevar":
            # Lógica para manejar pedidos para llevar
            print(f"Procesando pedido para llevar: {detalles}")
        elif tipo_pedido == "comer_en_local":
            # Lógica para manejar pedidos para comer en el local
            print(f"Procesando pedido para comer en el local: {detalles}")
        elif tipo_pedido == "entrega_a_domicilio":
            # Lógica para manejar pedidos de entrega a domicilio
            print(f"Procesando pedido de entrega a domicilio: {detalles}")
            
            # Si quisieramos añadir otro tipo de pedido tendríamos que modificar la clase.
            
        else:
            print("Tipo de pedido no válido")
         
         
# Código refactorizado.   
print("·"*35)
print(" ·· Refactorizado ..")

from abc import ABC, abstractmethod

#Clase maestra
class GestorPedidos(ABC):
    @abstractmethod
    def realizar_pedido(self, detalles):
        pass

class PedidoParaLlevar(GestorPedidos):
    def realizar_pedido(self, detalles):
        print(f"Procesando pedido para llevar: {detalles}")
        
class PedidoLocal(GestorPedidos):
    def realizar_pedido(self, detalles):
        print(f"Procesando pedido para comer en el local: {detalles}")
    
class EntregaADomicilio(GestorPedidos):
    def realizar_pedido(self, detalles):
        print(f"Procesando pedido de entrega a domicilio: {detalles}")
        
# Pedido añadido.
class PedidoEspecial(GestorPedidos):
    def realizar_pedido(self, detalles):
        print(f"Procesando pedido para evento especial: {detalles}")
        
class Restaurante:
    def __init__(self) -> None:
        self.gestor_pedido = []
        
    def registrar_pedidos(self, tipo_pedido:GestorPedidos):
        self.gestor_pedido.append(tipo_pedido)
        
    def realizar_pedido(self,tipo_pedido:GestorPedidos, detalles):
        tipo_pedido.realizar_pedido(detalles)
            
            
restaurante = Restaurante()
restaurante.registrar_pedidos(PedidoParaLlevar())
restaurante.registrar_pedidos(PedidoEspecial())
restaurante.realizar_pedido(PedidoParaLlevar(), "Plato de pasta.")
restaurante.realizar_pedido(PedidoEspecial(), "Pizza margarita.")