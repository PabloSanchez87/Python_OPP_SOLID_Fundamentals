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

