# Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)
"""
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
"""

""" Teoría - OCP - Open-Close Principle"""
# Abierto para la extensión, podemos añadir nuevas funcionalidades 
#   sin modificar lo existente.
# Cerrado para la modificación, el código que ya existe no debemos alterarlo.
""""""


                            ###############
                            ## EJERCICIO ##
                            ############### 
#  * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
#  * y crea un ejemplo simple donde se muestre su funcionamiento
#  * de forma correcta e incorrecta.    

# INCORRECTO
class Form:
    
    # def draw(self):
    def draw_square(self):
        print("Dibujamos un cuadrado.")
    
    def draw_circle(self):
        print("Dibujamos un círculo.")

    # A mayores ya tenemos más de una responsabilidad.

# CORRECTO                        
class From():
    def draw(self):
        pass
    
class Square(Form):
    def draw(self):
        print("Dibujamos un cuadrado.")

class Circle(Form):
    def draw(self):
        print("Dibujamos un círculo.")

class Triangle(Form):
    def draw(self):
        print("Dibujamos un triángulo.")
        
               
                            
                            ###############
                            ##   EXTRA   ##
                            ###############
# * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
# * Requisitos:
# *     - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
# * Instrucciones:
# *     1. Implementa las operaciones de suma, resta, multiplicación y división.
# *     2. Comprueba que el sistema funciona.
# *     3. Agrega una quinta operación para calcular potencias.
# *     4. Comprueba que se cumple el OCP.

#Importación de Módulos
from abc  import ABC, abstractmethod

# Definición de la Interfaz de Operación
# Creamos una interfaz llamada Operation utilizando una clase abstracta. 
# Esto asegura que cualquier operación que se quiera añadir debe implementar el método execute.
class Operation(ABC):
    
    @abstractmethod
    def execute(self, a, b):
        pass
    

# Implementación de las Operaciones
# Creamos varias clases que implementan la interfaz Operation 
#     para diferentes operaciones matemáticas
class Addition(Operation):
    def execute(self, a, b):
        return a + b

class Substration(Operation):
    def execute(self, a, b):
        return a - b 
    
class Multiplication(Operation):
    def execute(self, a, b):
        return a * b
    
class Division(Operation):
    def execute(self, a, b):
        if b != 0:
            return a / b
        else:
            return f"No se puede dividir entre 0."
              

# Implementación de la Calculadora
# Creamos una clase Calculator que mantiene un diccionario de operaciones. 
# Esto permite añadir nuevas operaciones sin modificar la clase Calculator, 
# cumpliendo con el principio de abierto/cerrado.
class Calculator:
    def __init__(self) -> None:
        self.operations = {}
        
    
    def add_operation(self, name, operation:Operation):
        self.operations[name] = operation
     
    
    def calculate(self,name, a, b):
        if name not in self.operations:
            raise ValueError (f"La operacion {name} no está soportada.")
        return self.operations[name].execute(a,b)
      
    
# Uso de la Calculadora
# Creamos una instancia de la calculadora y añadimos las operaciones disponibles
calculator = Calculator()
calculator.add_operation("addition", Addition())
calculator.add_operation("substration", Substration())
calculator.add_operation("multiplication", Multiplication())
calculator.add_operation("division", Division())

# Realizamos algunas operaciones con la calculadora
print(calculator.calculate("addition",10,2))
print(calculator.calculate("substration",10,2))
print(calculator.calculate("multiplication",10,2))
print(calculator.calculate("division",10,2))
print(calculator.calculate("division",10,0))



# Añadimos una nueva operación cumpliendo el principio de abierto y cerrado.
# Añadir una Nueva Operación
# Para añadir una nueva operación, simplemente creamos una nueva clase que 
# implemente Operation y la registramos en la calculadora
class Power(Operation):
    def execute(self, a, b):
        return a ** b 

calculator.add_operation("power", Power())
print(calculator.calculate("power",10,2))


# Documentación y Principio de Abierto/Cerrado
"""
El principio de abierto/cerrado establece que una clase debe estar abierta para 
la extensión pero cerrada para la modificación. 

En este ejemplo:

La clase Calculator está abierta para la extensión porque podemos añadir nuevas 
    operaciones sin modificar la clase.
    
La clase Calculator está cerrada para la modificación porque no necesitamos cambiar 
    su código interno para añadir nuevas operaciones.
"""