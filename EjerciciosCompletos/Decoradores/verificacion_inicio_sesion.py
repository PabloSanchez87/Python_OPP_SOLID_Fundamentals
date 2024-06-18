#Verificación de Inicio de Sesión con Decorado
"""
Estás desarrollando un sistema de autenticación para una aplicación web y
deseas implementar un sistema de inicio de sesión que verifique si las
credenciales proporcionadas por el usuario son válidas antes de permitir el
acceso a ciertas funciones. 
Además, deseas que una vez que el usuario haya iniciado sesión correctamente, 
se le proporcione información personal.

Implementa lo siguiente:
    1. Un registro de usuarios que contenga información adicional, como el
        nombre completo y el correo electrónico.
    2. Un decorador llamado verificar_inicio_sesion que acepte el nombre de
        usuario y la contraseña como argumentos. Este decorador verificará si las
        credenciales proporcionadas son válidas comparándolas con el registro de
        usuarios. Si las credenciales son válidas, la función decorada se ejecutará y
        se le pasará como argumento la información personal del usuario.
    3. Una función llamada informacion_usuario que imprima la información personal
        del usuario después de que haya iniciado sesión correctamente.

Implementa este sistema de inicio de sesión utilizando decoradores.       
"""

users_registrados = {
    "usuario1": {"contraseña": "contraseña123", "nombre_completo": "Juán Pérez", "correo_electronico": "juan@correo.com"},
    "usuario2": {"contraseña": "contraseña456", "nombre_completo": "María Gómez", "correo_electronico": "maria@correo.com"},
    "usuario3": {"contraseña": "contraseña789", "nombre_completo": "Carlos Rodríguez", "correo_electronico": "carlos@correo.com"},
}


def verificar_inicio_sesion(function):
    def wrapper(nombre_user, password):
        if nombre_user in users_registrados and users_registrados[nombre_user]['contraseña']==password:
            print(f"Inicio de sesión exitoso para el usuario {nombre_user}")
            usuario_info = users_registrados[nombre_user]
            return (function(usuario_info))
        else:
            print(f"Error en el inicio de sesion del {nombre_user}.")
    return wrapper
        
        
@verificar_inicio_sesion
def informacion_usuario(user_info):
    print("Información personal del usuario:")
    print(f" · Nombre completo: {user_info['nombre_completo']}.")
    print(f" · Correo electrónico: {user_info['correo_electronico']}.")
    
print("·"*40)
informacion_usuario("usuario1", "contraseña123")
print("·"*40)
informacion_usuario("usuario2", "contraseña123")
print("·"*40)
informacion_usuario("usuario2", "contraseña456")
print("·"*40)
informacion_usuario("usuario_2", "contraseña456")