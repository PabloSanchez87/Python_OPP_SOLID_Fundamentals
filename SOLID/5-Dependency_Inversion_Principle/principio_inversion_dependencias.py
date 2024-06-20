## SOLID
# Single Responsability PRinciple
# Open/Closed Principle
# Liskov's Substitution Principle
# Interface Segregation Principle
# Dependency Inversion Principle
"""
Conjunto de reglas y mejores prácticas a seguir al diseñar
una estructura de clase.

Autor: Robert J. Martin

Sirven para crear un código comprensible, legible y comprobable
en el que muchos desarrolladores pueden trabajar en colaboración.
"""
# Dependency Inversion Principle
""" Definición.
- Los módulos de alto nivel no deberían depender de los módulos 
    de bajo nivel. Ambos deberían depender de abstracciones.
- Las abastracciones no deberían depender de los detalles. 
    Los detalles deberían depender de las abstracciones.
"""

# Concepto. Módulos de Alto Nivel.
""" Concepto. Módulos de Alto Nivel.
- Las clases que manejan y gestionan la lógica de negocios.
  No va a los detalles.
"""
class App:
    def __init__(self, notificador: Notificador) -> None:
        self.notificador = notificador
    def enviar_notificacion(self, mensaje:str):
        self.notificador.enviar(mensaje)
        print("Notificación enviada correctamente.")  
# Concepto. Módulos de bajo nivel.
""" Concepto. Módulos de bajo nivel.
- Clases que implementan los detalles.
"""
class EmailNotificador(Notificador):
    def enviar(self, mensaje:str):
        print(f"Enviando email: {mensaje}")
        

# Concepto. Abstracciones.
""" Concepto. Abstracciones.
- Estas son interfaces o clases abstractas que definen los métodos 
    que los módulos de alto y bajo nivel deben implementar.
- Ejemplo: una interfaz Notificador que declara 
    un método enviar(mensaje:str)
"""
# Beneficios.
""" Beneficios.
    - Reduccion del acoplamiento. Dependemos de abstraciones y 
        no implementaciones.
    - Mejora la modularidad.
    - Facilita el testing. 
          Ejemplo. Si tenemos una clase que es el almacenamiento de los datos, 
          que depende de una base de datos, pero no de una específica 
          (dependemos de una abastracción). 
          Cuando querramos testear esa clase, podemos enviar cualquier tipo de BD,
          y la clase no tendrá ningún problema pq será la abstracción que espera.
    - Mantenibilidad y extensibilidad.
"""

# RESUMEN
""" Comparación con otros Principios SOLID.
    - Responsabilidad única
        · Se complementan pq promueven la separación de responsabilidades 
            y reducen el acoplamiento.
    - Principio abierto/cerrado (OCP)
        · Refuerza el principio de inversión de dependencias.
    - Principio de sustitución de Liskov (LSP)
        · Facilita el LSP pq promueve las abstracciones.
    - Principio de Segregación de Interfaces (ISP)
        · Trabajan juntos para asegurar que las clases de alto nivel dependan de 
            interfaces específicas y mínimas. Buscan las clases lo más pequeñas 
            posibles.
    
    Nota. DIP es fundamental para la implemntación de los otros principios SOLID:
        - Ayuda a mantener el código abierto para la extensión (OCP)
        - Garantiza que las implementaciones puedan ser sustituidas (LSP)
        - Promueve interfaces específicas (ISP).
        - Mantiene las responsabilidades claras (SRP)
"""

# TÉCNICAS.
""" 
Técnicas de Inyección de Dependencias - Inyección de Constructor """
""" 
Nosotros le damos a la clase que requiera la abstracción 
la dependencia que requeire.
"""
from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass
    
class EmailNotificador(Notificador):
    def enviar(self, mensaje: str):
        print(f'Enviando email: {mensaje}')
        
## App es la que maneja la lógica de negocios.        
class App: 
    # Depende de una abstracción de Notificador.
    def _init_(self, notificador: Notificador):
        self.notificador = notificador

    def enviar_notificacion(self, mensaje: str):
        self.notificador.enviar(mensaje)
        print("Notificación enviada correctamente.")
        
notificador = EmailNotificador()
app = App(notificador)
app.enviar_notificacion("Hola Mundo!")


# TÉCNICAS.
""" Técnicas de Inyección de Dependencias - Inyección de Setter (Método) """
""" La recibimos por el set notificador que depende la 
abstracción de Notificador"""
class App:
    def init_(self):
        self.notificador = None

    def set_notificador(self, notificador: Notificador):
        self.notificador = notificador

    def enviar_notificacion(self, mensaje: str):
        if self.notificador:
            self.notificador.enviar(mensaje)
            print("Notificación enviada correctamente.")
        else:
            print("Notificador no configurado.")

app = App()
notificador = EmailNotificador()
app.set_notificador(notificador)
app.enviar_notificacion("Hola Mundo!")


# TÉCNICAS.
""" Técnicas de Inyección de Dependencias - Inyección de Método"""
""" Similar al método setter pero puede ser cualquier método."""
class App:
    def enviar_notificacion(self, notificador: Notificador, mensaje: str):
        notificador.enviar(mensaje)
        print("Notificación enviada correctamente.")

app = App()
notificador = EmailNotificador()
app. enviar_notificacion(notificador, "Hola Mundo!")