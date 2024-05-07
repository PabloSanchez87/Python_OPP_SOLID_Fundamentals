class Empleado:
    numero_empleados = 0 # Atributo de clase

    # Creacion del CONSTRUCTOR
    # nombre, cargo, salario --> atributo de instancia.
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        Empleado.numero_empleados += 1  # Incrementamos el atributo de la clase con cada nueva instancia

# COMPORTAMIENTO
    # Método de instancia
    def presentarse(self):
        print(f"Hola me llamo {self.nombre} y ocupo el cargo de {self.cargo}")
    # Método de instancia
    def aumentar_salario(self, porcentaje):
        self.salario *= 1 + porcentaje/100
        print(f"Nuevo salario de {self.nombre}: {self.salario}")

# DECORADOR DE MÉTODO DE LA CLASE
    @classmethod
    def desde_string(cls, datos_empleado):
        nombre,cargo,salario =  datos_empleado.split(",")
        return cls(nombre, cargo, float(salario))
    
    # El método estático de la clase, pero no tiene acceso ni dependen de los métodos ni atributos de la instancia. 
    @staticmethod
    def es_festivo(dia):
        vacaciones = [1,10,27]
        return dia in vacaciones # Devuelve true o false según sean vacaciones o no.


## INSTANCIAR UNA CLASE 
# Usando un método de instancia
empleado1 = Empleado("Pablo Sanchez", "Gerente", 5000)
empleado2 = Empleado("Laura Asorey", "Funcionaria", 3500)

# Usando un método de la clase
empleado3 = Empleado.desde_string("Torres Souto,Observador,3000")

# Utilizando un método estático.
print(Empleado.es_festivo(1))

# Utilizamos los métodos de instancia.
empleado1.presentarse()
empleado1.aumentar_salario(10)
empleado2.presentarse()
empleado3.presentarse()

# Acceso a un atributo de la clase.
print(Empleado.numero_empleados)

