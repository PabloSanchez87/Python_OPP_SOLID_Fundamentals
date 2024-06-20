class Figura:
    def obtener_area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, ancho, alto) -> None:
        self.ancho = ancho
        self.alto = alto
    
    def obtener_area(self):
        return self.alto * self.ancho
    
    def set_ancho(self, ancho):
        self.ancho = ancho
        
    def set_alto(self, alto):
        self.alto = alto
        
class Cuadrado(Figura):
    def __init__(self, lado) -> None:
        self.lado = lado
        
    def set_lado(self, lado):
        self.lado = lado  

    def obtener_area(self):
        return self.lado * self.lado
        
def imprimir_area(figura:Figura):
    print(f"Área: {figura.obtener_area()}")

rectangulo = Rectangulo(4,5)
cuadrado = Cuadrado(4)

print("·"*20)
imprimir_area(rectangulo)
imprimir_area(cuadrado)

print("·"*20)
rectangulo.set_alto(6)       
rectangulo.set_ancho(7)
imprimir_area(rectangulo)

cuadrado.set_lado(5)
imprimir_area(cuadrado)
print("·"*20)


# Nota. 
# Debemos cumplir que el padre sea representante del hijo como que el hijo 
# pueda sustituir el padre sin tener que modificar el código.
# El hijo debe implementar completamente al padre.