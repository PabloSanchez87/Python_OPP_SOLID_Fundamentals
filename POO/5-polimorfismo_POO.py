## POLIMORFISMO
# Concepto de la POO que se refiere a la capacidad de diferentes objetos de
# responder de manera diferente a la misma invocación de método.
    # FLEXIBILIDAD EN EL CÓDIGO
        # Permite escribir código más flexible y genérico al tratar objetos
        # de diferentes clases de manera uniforme si comparten una interfaz común.
    # FACILITA LA EXTENSIÓN DEL SOFTWARE
        # Nuevas clases pueden implementar la misma interfaz que las clases existentes
        # y ser utilizadas en el mismo contexto.

class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio) -> None:
        self.radio = radio
    
    def area(self):
        return 3.14 * self.radio**2
    
class Cuadrado(Figura):
    def __init__(self, lado) -> None:
        self.lado = lado

    def area(self):
        return self.lado**2
    

def calcular_area(figura):
    return figura.area()

circulo = Circulo(5)
cuadrado = Cuadrado(10)

print(f"Área de un círculo: {calcular_area(circulo)}")
print(f"Área de un cuadrado: {calcular_area(cuadrado)}")