"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""

class Polygon:
    def __init__(self, lado:float) -> None:
        self.lado = lado

class Cuadrado(Polygon):
    def __init__(self, lado: float) -> None:
        super().__init__(lado)

    def area(self):
        return self.lado * self.lado

class Triangulo(Polygon):
    def __init__(self, lado: float, altura:float) -> None:
        super().__init__(lado)
        self.altura = altura

    def area(self):
        return (self.lado * self.altura)/2
    
class Rectangulo(Polygon):
    def __init__(self, lado: float, lado_largo:float) -> None:
        super().__init__(lado)
        self.lado_largo = lado_largo

    def area(self):
        return self.lado * self.lado_largo
    

cuadrado = Cuadrado(5)
triangulo = Triangulo(2,2.5)
rectangulo = Rectangulo(2,4)

print("Área del cuadrado:",cuadrado.area())
print("Área del triángulo:",triangulo.area())
print("Área del rectángulo:",rectangulo.area())

        

