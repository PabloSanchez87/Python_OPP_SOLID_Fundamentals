## SOLID
# Single Responsability PRinciple
# Open/Closed Principle
# Liskov's Substitution Principle
# Interface Segregation Principle
# Dependency  Inversion Principle
"""
Conjunto de reglas y mejores prácticas a seguir al diseñar
una estructura de clase.

Autor: Robert J. Martin

Sirven para crear un código comprensible, legible y comprobable
en el que muchos desarrolladores pueden trabajar en colaboración.
"""
# Interface Segregation Principle (ISP)
""" Definición:
No se debe obligar a los clientes a depender de métodos que no utilizan. 
Las interfaces pertenecen a clientes, no a jerarquías.
"""
""" Definición:
Si una clase no utiliza métodos o atributos particulares, entonces esos 
métodos y atributos deben segregarse en clases más específicas.
"""
""" Definición: Interfaz
En la POO, un interfaz define al conjunto de métodos que tienen que tener un 
objeto para que pueda cumplir una determinada función en nustros sistema. 
Dicho de otra manera, un interfaz define como se comporta un objeto y lo que
puede hacer con él. Es un contrato que se debe cumplir.
"""
""" Beneficios:
    - Mantenimiento.
    - Flexibilidad.
    - Reutilización.
"""

# ATENCIÓN: Nuevo estándar en Python para las interfaces.
""" Protocol (typing.protocol):
Un protocolo es un conjunto de métodos o atributos que un objeto debe tener para 
ser considerado compatible con ese protocolo. Los protocolos le permiten definir 
interfaces sin crear explícitamente una clase o heredar de una clase base específica.
"""

""""""
# NOTA. Solemos poner la letra I delante del nombre de la clase para 
# indicar que es una interfaz.
# IVehicle, IMando, ...
""""""

# Interfaz informal: No estamos obligando a cumplir el contrato a MandoLG.
class MandoInformal:
    def siguietne_canal(self):
        pass
    def canal_anterior(self):
        pass
    def subir_volumen(self):
        pass
    def bajar_volumen(self):
        pass
class MandoLG(MandoInformal):
    pass

""""""
# Interfaz formal: Nos obliga a implementar todos los métodos.
# Una clase abstract no podemos inicilizarla. Sólo implementarla en subclases.
from abc import ABCMeta, abstractmethod

class IMandoFormal(metaclass=ABCMeta):
    @abstractmethod
    def siguietne_canal(self):
        pass
    @abstractmethod
    def canal_anterior(self):
        pass
    @abstractmethod
    def subir_volumen(self):
        pass
    @abstractmethod
    def bajar_volumen(self):
        pass

class MandoSansung(IMandoFormal):
    def siguietne_canal(self):
        print("Siguiente canal")
    def canal_anterior(self):
        print("Anterior canal")
    def subir_volumen(self):
        print("Subir volumen")
    def bajar_volumen(self):
        print("Bajar volumen")
        
""""""




        