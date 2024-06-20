# Ejemplo de aplicación con notificación.
from abc import ABC, abstractmethod

# Abstracción para el servicio de notificación (interface)
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje:str):
        pass
    
# Implementación del servicio de notificacion correo electrónico.
# Clase de BAJO NIVEL QUE DEPENDE UNA ABSTRACCIÓN 
#          Y NO DE UNA IMPLEMENTACIÓN
class EmailNotificador(Notificador):
    def enviar(self, mensaje:str):
        print(f"Enviando email: {mensaje}")


# Implementación del servicio de notificacion sms
# Clase de BAJO NIVEL --> Incluye detalles.
class SmsNotificador(Notificador):
    def enviar(self, mensaje:str):
        print(f"Enviando sms: {mensaje}")
        

# Clase o módulo de ALTO NIVEL que maneja la lógica de negocios.
#   Dependerá de abstracciones tmb. Quiero depender de la abstracción para 
#   poder inyectar cualquier método que la implemente.
class App:
    def __init__(self, notificador : Notificador) -> None: # inversión de dependencias
        self.notificador = notificador
        
    def enviar_notificacion(self, mensaje: str):
        self.notificador.enviar(mensaje)
        print(f"Notificación enviada correctamente.")
        


# MODO DE USO
email_notificador = EmailNotificador()
app_con_email = App(email_notificador) ## inyección de dependencias.
app_con_email.enviar_notificacion("Este es un mensaje de prueba de correo electrónico.")

sms_notificador = SmsNotificador()
sms_notificador = App(sms_notificador) ## inyección de dependencias.
sms_notificador.enviar_notificacion("Este es un mensaje de prueba de sms.")