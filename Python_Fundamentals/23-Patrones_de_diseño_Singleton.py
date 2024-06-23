# PATRONES DE DISEÑO - SINGLETON
""" 
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
"""
## Página para repasar patrones de diseño.
# https://refactoring.guru/es/design-patterns
""" 
Singleton - Instancia única
DEFINICION:
    Patrón de diseño creacional que nos permite asegurarnos de que una clase tena 
    una única instancia, a la vez que proporciona un punto de acceso global a 
    dicha instancia.
PROBLEMA A RESOLVER:
    Resuelve dos problemas, vulnerando el principio de responsabilidad única:
    1. Garantizar que una clase tenga una única instancia.
        - Motivo más habitual: Controlar el acceso a algún recurso compartido.
        - Ejemplo: BBDD    
    2. Proporcionar un punto de acceso a dicha instancia.
        - Singleton nos permite acceder a un objeto desde cualquier parte. 
            No obstante, tambien evita que otro código sobreescriba esa instancia.
        - Problema. No queremos que el código que secuelvve el primer problema se
            encuentre disperso por todo el programa. Es mucha más conveniente tenerlo
            dentro de una clase, sobre todo si el resto del código ya depende de ella.
SOLUCIÓN PLANTEADA:
    Todas las implementaciones del patrón Singleton tienen estos dos pasos en común:
        - Hacer privado el constructor por defecto para evitar que otros objetos 
            utilicen el operardor new con la clases Singleton
        - Crear un método de creación estático que actúe como contructor.
            Este método invoca al contructor privado para crear un objeto y lo guarda 
            en un campo estático.
            Las siguientes llamadas a este método devuelven el objetos almacenado en
            caché.    
"""

                            ###############
                            ## EJERCICIO ##
                            ############### 
#  * Explora el patrón de diseño "singleton" y muestra cómo crearlo
#  * con un ejemplo genérico.

class Singleton:
    _instance = None
    
    # Constructor de clase, para crear la instancia.
    # Si no existe la instancia creada, creamos la instancia.
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
    
singleton1 = Singleton()
print(singleton1)
singleton2 = Singleton()
print(singleton2)  # Nos devuelve el mismo objeto.
print(f"Singleton1 es Singleton2 = {singleton1 is singleton2}")


                            ###############
                            ##   EXTRA   ##
                            ############### 
#  * DIFICULTAD EXTRA (opcional):
#  * Utiliza el patrón de diseño "singleton" para representar una clase que
#  * haga referencia a la sesión de usuario de una aplicación ficticia.
#  * La sesión debe permitir asignar un usuario (id, username, nombre y email),
#  * recuperar los datos del usuario y borrar los datos de la sesión.

print("·"*50)
class UserSesion:
    _instance = None
    id: int = None
    username :str = None
    name: str = None
    email: str = None
 
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSesion, cls).__new__(cls)
        return cls._instance
    
    def set_user(self, id, username, name, email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email
        
    def get_user(self):
        return f"{self.id}, {self.username}, {self.name}, {self.email}."
    
    def clear_user(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None
        

session1 = UserSesion()
session1.set_user(1, "PabloST", "Pablo", "pablo@gmail.com")
print(session1)
print(session1.get_user())

session2 = UserSesion()
print(" ·· Session2 tiene acceso a los datos de la sesión común! ·· ") 
print(session2.get_user())

session3 = UserSesion()
session3.clear_user() ## Reinicializamos todos los valores. S
print(session3.get_user())
print(session1.get_user())
print(session2.get_user())

# Nos aseguramos de que solo tengamos una sessión activa.
# Ejemplo. El carrito de compra seguramente cumpla un patrón singleton
#           EL carrito se mantiene a pesar de que naveges por la app.