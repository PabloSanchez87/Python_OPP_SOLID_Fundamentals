## La herencia permite que una clase hija herede atributos y métodos
#  de una clase padre. Esto promueve la reutilizción y la jerarquía de clases.
        # Reutilización de código
            # Promueve la reutilización y evitar la duplicación de funcionalidades.
        # Estructura jerárquica
            # Clases más específicas (subclases) pueden heredar característsicas
            # de clases más generales (superclases)
        # Abstracción de comportamiento común
            # La herancia facilita de clases que encapsulan comportamientos comunes.

class Vehiculo:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"Este vehículo es de la marca: {self.marca} y modelo: {self.modelo}"
    
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas) -> None:
        super().__init__(marca, modelo)
        self.puertas = puertas

    def describir(self):
        return f"Este automóvil es de la marca: {self.marca}, modelo: {self.modelo} con {self.puertas} puertas."
    
class Camion(Automovil):
    def __init__(self, marca, modelo, puertas, carga) -> None:
        super().__init__(marca, modelo, puertas)
        self.carga = carga

    def describir(self):
        return f"Este automóvil es de la marca: {self.marca}, modelo: {self.modelo} con {self.puertas} puertas y capacidad de carga {self.carga} kg."
    

info_vehiculo1 = vehiculo1 = Automovil("Mercedes", "GLA 220d", 5)
info_vehiculo2 =  vehiculo2 = Camion("Toyota", "QWERTY", 2 , 1500)

print(info_vehiculo1.describir())
print(info_vehiculo2.describir())