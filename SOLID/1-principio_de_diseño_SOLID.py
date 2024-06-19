## PRINCIPIOS DE DISEÑO ##

# Qué son?
""" 
Los principios de diseño en software son directrices generales que 
ayudan a los desarrolladores a crear sistema de software que sean
fáciles de entendes, mantener y extender.
"""

# Cohesión
""" 
La cohesión se refiere a la medida en que las responsabilidades
y funciones de un módulo (clase, método o componente) están 
relacionadas y enfocadas en una única tarea o porpósito.
"""

# Acoplamiento
""" 
Grado de interdependencia entre los diferente módulos de un
sistema.
"""

# NOTA
## Se busca alta cohesión con el menor acoplamiento posible.
# ALTA COHESIÓN
""" 
    - Facilita la comprensón del código.
    - Promueve la reutilización de código.
    - Simplifica las pruebas y mantenimiento.
"""
# BAJO ACOPLAMIENTO
""" 
- Permite que los módulos sean más independientes.
- Facilita el mantenimiento y la evolución del código.
- Promueve la modularidad y la separación de preocupaciones.
"""

###  Ejemplo.  ###
class Usuario:
    def __init__(self, nombre, email) -> None:
        self.nombre = nombre
        self.email = email
        
    def enviar_correo(self, asunto, mensaje):
        print(f"Enviado correo a {self.email} con asunto {asunto} y mensaje : {mensaje}")
        
    def guardar_registro(self, accion):
        print(f"Guardando registro de acción: {accion}")
        
        
class GestorUsuarios:
    def __init__(self) -> None:
        self.usurios = []
        
    def agregar_usuario(self, nombre, email):
        usuario = Usuario(nombre, email)
        self.usurios.append(usuario)
        usuario.enviar_correo("Bienvenido", "Gracias por registrarte.")
        usuario.guardar_registro("Registro de usuario")
        
# Ejemplo de uso.
gestor_usuarios = GestorUsuarios()
gestor_usuarios.agregar_usuario("Juan", "juan@correo.com")

print("·"*60)

### Ejemplo 2 mejorado respecto a alta cohesión y bajo acoplamiento ###
print(" ·· Alta cohesión y bajo acoplamiento ···")
print(" · "*20)  
    
class Usuario:
    def __init__(self, nombre, email) -> None:
        self.nombre = nombre
        self.email = email
      
        
class GestorCorreo:        
    def enviar_correo(self,destinatario, asunto, mensaje):
        print(f"Enviado correo a {destinatario} con asunto {asunto} y mensaje : {mensaje}")
    
    
class RegistroAcciones:
    def guardar_registro(self, accion):
        print(f"Guardando registro de acción: {accion}")
        

class GestorUsuarios:
    def __init__(self, gestor_correo:GestorCorreo, registro_accion:RegistroAcciones) -> None:
        self.usurios = []
        self.gestor_correo = gestor_correo
        self.registro_accion = registro_accion
        
    def agregar_usuario(self, nombre, email):
        usuario = Usuario(nombre, email)
        self.usurios.append(usuario)
        self.gestor_correo.enviar_correo(usuario.email, "Asunto: registro #34", "Gracias por registrarte.")
        self.registro_accion.guardar_registro(f"Registro de usuario.")
        
    
# Ejemplo de uso
gestor_correo = GestorCorreo()
registro_accion = RegistroAcciones()
gestor_usuarios = GestorUsuarios(gestor_correo, registro_accion)
gestor_usuarios.agregar_usuario("Juan", "juan@correo.com")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

