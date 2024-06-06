#################################
#### HERENCIA VS COMPOSICIÓN ####
#################################
    # Herencia vs Composición.
    # Principios de diseño.
    # Cohesión.
    # Acoplamiento.

''' # Herencia: es un/a --> relación unidireccional, permanente.'''
    # VENTAJAS:
        # Reutilización de codigo.
        # Polimosfirmos.
        # Sobreescritura de métodos.
        # Desarrollo guiado. Patrón. Template.
    # DESVENTAJAS:
        # Proyectos ágiles. --> Al inicio es difícil conocer la evolución del proyecto.
        # "la fiesta del override". --> Una clase hija sobreescribe de forma excesiva la clase padre.
        # "la herencia de 7 niveles". --> Clases que heredan de demasiadas clases.
    # Cuando usar herencia:
        # Existe una relación de tipo "es un/a" clara y permanente.
        # Se busca reutilizar código y comportamiento común.
        # Se necesita polimorfismo estático.
        # Se modela el dominio del problema.
        
''' # Composición: Quiere decir que tenemos una instancia de una clase que contiene instancias '''
    #              de otras clases que implementas las funciones deseadas.
    # VENTAJAS:
        # Versatilidad. Más libertad.
        # Creación/destrucción dinámica. 
        # Polimorfismo mediante interfaces.
    # Cuando usar composición:
        # No existe una relación del tipo "es un/a" clara y permanente.
        # Se necesita flexibilidad y capacidad de cambio.
        # Se busca desacoplar y reutilizar componentes.
        # Se requiere implementar comportamientos intercambiables.
        # Se tiene una relación de tipo "tiene un".

# Ejemplo 1. Herencia.
class Animal:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    def hacer_sonidos(self):
        pass

class Conejo(Animal):
    def hacer_sonidos(self):
        return "Soy un conejo."
    
conejo = Conejo("Zanahoria")
print(conejo.nombre)
print(conejo.hacer_sonidos())


# Ejemplo 2. Herencia multiple, dejan de tener una relación tan estrecha.
class Vehiculo:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo

    def conducir(self):
        return "Rum rum!!"

class Persona(Vehiculo, Animal):
    def __init__(self,nombre, marca, modelo) -> None:
        Vehiculo.__init__(self, marca, modelo)
        Animal.__init__(self, nombre)

    def presentarse(self):
        return f"Soy {self.nombre}, conduzco un {self.marca} {self.modelo}"


persona1 = Persona("Juan", "Toyota", "Corolla")
print(persona1.presentarse())
print(persona1.conducir())

## Ejemplo 3. Clases con composición
print("\n Composición...")

class PersonaComposicion:
    def __init__(self, nombre, vehiculo, animal):
        self.nombre = nombre
        self.vehiculo = vehiculo
        self.animal = animal
    
    def presentarse(self):
        return f"Soy {self.nombre}, conduzco un {self.vehiculo.marca} {self.vehiculo.modelo} y mi mascota es {self.animal.nombre}."
    
vehiculo2 = Vehiculo("Mercedes", "GLA 220d")
animal2 = Animal("Ruffy")
persona2 = PersonaComposicion("Pablo", vehiculo2, animal2)
print(persona2.presentarse())
print(persona2.vehiculo.conducir())






