# Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)
"""
EJERCICIO:
Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
DIFICULTAD EXTRA (opcional):
Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
cumplir el LSP.
Instrucciones:
    1. Crea la clase Vehículo.
    2. Añade tres subclases de Vehículo.
    3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
    4. Desarrolla un código que compruebe que se cumple el LSP.
"""

""" Teoría - LSP - Liskov Substitution Principle"""
# Establece que si tenemos una clase y esa clase tiene clase(s) derivada(s) 
# los objetos de la clase base (clase padre) los podemos alternar sin que 
# el funcionamiento del programa sea incorrecto. 
""""""


                            ###############
                            ## EJERCICIO ##
                            ############### 
# Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
# y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.

#* INCORRECTO
class Bird:
    def fly(self):
        return f"Flying"
    
class Chicken(Bird):
    def fly(self):
        raise Exception("Chicken can't fly")
    
# bird = Bird()
# bird.fly()
# chicken = Chicken()
# chicken.fly()

#* CORRECTO
class Bird:
    def move(self):
        return f"Moving"
    
class Chicken(Bird):
    def move(self):
        return "Walk"
    
bird = Bird()
print(bird.move())
chicken = Chicken()
print(chicken.move())

bird = Chicken()
print(bird.move())
chicken = Bird()
print(chicken.move())
        
        
print("·"*30)                     
                            ###############
                            ##   EXTRA   ##
                            ###############
# Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
# cumplir el LSP.
# Instrucciones:
#     1. Crea la clase Vehículo.
#     2. Añade tres subclases de Vehículo.
#     3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
#     4. Desarrolla un código que compruebe que se cumple el LSP.

# Clase base Vehículo
class Vehicle:
    def __init__(self, speed=0) -> None:
        self.speed = speed
    
    def accelerate(self, increment):
        # Incrementar la velocidad
        self.speed += increment 
        print(f"· Velocidad: {self.speed} Km/h")
        
    def brake(self, decrement):
        # Reducir la velocidad, asegurando que no sea negativa
        self.speed -= decrement
        if self.speed <= 0:
            self.speed =0
        print(f"· Velocidad: {self.speed} Km/h")
        
        
# Subclase Car que hereda de Vehicle        
class Car(Vehicle):
    def accelerate(self, increment):
        # Mensaje específico para Car
        print(f"The {self.__class__.__name__} is accelerating.")
        # Llama al método de la clase base
        super().accelerate(increment)
    
    def brake(self, decrement):
        # Mensaje específico para Car
        print(f"The {self.__class__.__name__} is braking.")
        # Llama al método de la clase base
        super().brake(decrement)
    

# Subclase Bicycle que hereda de Vehicle
class Bicycle(Vehicle):
    def accelerate(self, increment):
        print(f"The {self.__class__.__name__} is accelerating.")
        super().accelerate(increment)
    
    def brake(self, decrement):
        print(f"The {self.__class__.__name__} is braking.")
        super().brake(decrement)
    

# Subclase Motorcycle que hereda de Vehicle
class Motorcycle(Vehicle):
    def accelerate(self, increment):
        print(f"The {self.__class__.__name__} is accelerating.")
        super().accelerate(increment)
    
    def brake(self, decrement):
        print(f"The {self.__class__.__name__} is braking.")
        super().brake(decrement)
        
        
# Función de prueba que toma cualquier objeto de tipo Vehicle
def test_vehicle(vehicle:Vehicle):
    vehicle.accelerate(2)
    vehicle.brake(1)
    print("----")


# Crear instancias de cada tipo de vehículo
car = Car()
bicycle = Bicycle()
motorcycle =Motorcycle()

# Probar cada instancia para verificar que cumplen con LSP
test_vehicle(car)
test_vehicle(bicycle)
test_vehicle(motorcycle)


#? Cumplimiento del LSP:
# · El Principio de Sustitución de Liskov (LSP) establece que los objetos de una
#       subclase deben ser sustituibles por objetos de la clase base sin afectar el 
#       funcionamiento del programa.
# · En este código, Car, Bicycle y Motorcycle son subclases de Vehicle y se 
#       comportan de manera intercambiable en la función test_vehicle.
# · Esto demuestra que las subclases cumplen con el contrato definido por la clase 
#       base Vehicle, respetando el LSP.





