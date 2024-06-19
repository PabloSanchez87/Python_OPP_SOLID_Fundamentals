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
# Single Responsibility Principle - Principio de responsabilidad única
""" Una clase debe hacer una cosa y, por lo tanto, debe tener una
sola razón para cambiar.
    - Claridad de la responsabilidad.
    - Facilita el mantenimiento.
    - Promueve la cohesión.
    - Facilita la reutilización del código.
"""
# Ejemplo mala estructura.
""" 
class Factura:
    factura()
    calculaTotal()
    imprimeFactura()
    guardarFactura()
"""
# Ejemplo estructura SOLID.
""" 
class Factura:
    factura()

class FacturaImpresion:
    facturaImpresion()
    imprimir()
    
class FacturaGuardado:
    facturaGuardado()
    guardarArchivo()
"""


## Ejemplo de uso.

## Código acoplado
class Engine:
    def __init__(self):
        pass

    def getRPM(self):
        return 3000


class Vehicle:
    def __init__(self, name, speed):
        self._name = name
        self._speed = speed
        self._engine = Engine()

    def getName(self):
        return self._name

    def getEngineRPM(self):
        return self._engine.getRPM()

    def getMaxSpeed(self):
        return self._speed

    def printInfo(self):
        print(
            "Vehicle: {}, Max Speed: {}, RMP: {}".format(
                self._name, self._speed, self._engine.getRPM()
            )
        )

if __name__ == "__main__":
    vehicle = Vehicle("Car", 200)
    vehicle.printInfo()
    
    
## Código SOLID - Refactorizado.
print("·"*40)
print(" ·· Refactorizado ..")

class Engine:
    def getRPM(self):
        return 3000
    
class Vehicle:
    def __init__(self,name, speed, engine:Engine) -> None:
        self._name = name
        self._speed = speed
        self._engine = engine
        
    def getName(self):
        return self._name
    
    def getEngineRPM(self):
        return self._engine.getRPM()
    
    def getMaxSpeed(self):
        return self._speed

class VehiclePrinter:
    def __init__(self, vehicle:Vehicle) -> None:
        self._vehicle = vehicle
        
    def printInfo(self):
        print(f"Vehicle: {self._vehicle.getName()}, " 
              f"Max Speed: {self._vehicle.getMaxSpeed()}, "
              f"RPM: {self._vehicle.getEngineRPM()}")
        
# Añadimos otra clase.
class VehiclePersistance:
    def __init__(self, vehicle:Vehicle, db) -> None:
        self._vehicle = vehicle
        self._persistence = db
        print(f"Hey, storing data in {self._persistence}")


if __name__ == "__main__":
    engine = Engine()
    vehicle = Vehicle(name="Car", speed=200, engine=engine)
    persistance = VehiclePersistance(vehicle, db="Firabase")
    printer = VehiclePrinter(vehicle=vehicle)
    printer.printInfo()


## Notas.
# Es normal que acabemos teneniendo un código más largo.
    
    