"""
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""
## HERENCIA
class Animal: # Clase PADRE
    def __init__(self, name:str) -> None:
        self.name = name

    def sound(self):
        pass


# SUBCLASES
class Dog(Animal):

    #sobrecargamos método sound. POLIMORFISMO EN TIEMPO DE EJECUCIÓN
    def sound(self):
        print("Guau!")

class Cat(Animal):

    #sobrecargamos método sound. POLIMORFISMO EN TIEMPO DE EJECUCIÓN
    def sound(self):
        print("Miau!")

# Polimorfismo EN COMPILACIÓN
def print_sound(animal:Animal):
    animal.sound()

my_animal = Animal("Animal")
print_sound(my_animal)
my_dog = Dog("Paulov")
my_dog.sound()
print_sound(my_dog)
my_cat = Cat("Pelusa")
my_cat.sound()
print_sound(my_cat)

### EXTRA ###
class Employee:
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)
    
class Manager(Employee):
    def coordinate_projects(self):
        print(f"{self.name} está coordinando todos los proyectos.")


class ProjectManager(Employee):
    def __init__(self, id: int, name: str, project:str):
        super().__init__(id, name)
        self.project = project

    def coordinate_project(self):
        print(f"{self.name} está coordinando su proyecto.")


class Programmer(Employee):
    def __init__(self, id: int, name: str, language:str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} está programando en {self.language}")

    def add(self, employee:Employee):
        print(f"Un programador no tiene empleados a su cargo. {employee.name} no se añadirá.")


my_manager = Manager(1, "Pablo")
my_project_manager1 = ProjectManager(2, "PabloPro","Proyect1")
my_project_manager2 = ProjectManager(3, "LauraPro","Proyect2")
my_programmer1 = Programmer (4,"PabloDev", "Python")
my_programmer2 = Programmer (5,"PauDev", "Java")
my_programmer3 = Programmer (6,"RoiDev", "JS")
my_programmer4 = Programmer (7,"AntonDev", "Angular")

my_manager.add(my_project_manager1)
my_manager.add(my_project_manager2)

my_project_manager1.add(my_programmer1)
my_project_manager1.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)

my_programmer1.add(my_programmer2)

my_programmer1.code()
my_project_manager1.coordinate_project()
my_manager.coordinate_projects()
my_manager.print_employees()
my_project_manager1.print_employees()
my_programmer1.print_employees()

    