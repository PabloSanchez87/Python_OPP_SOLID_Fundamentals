# Decorador de Control de Acceso
"""
Imagina que estás trabajando en el desarrollo de un sistema para una
aplicación de gestión de documentos en un entorno empresarial.
 
Deseas implementar un decorador llamado verificar_acceso_entorno que permita
controlar el acceso a funciones según el entorno de ejecución.

El decorador debe realizar las siguientes acciones:
    1. Antes de ejecutar la función, verificar si el entorno de ejecución es
        "producción".
    2. Si el entorno es "producción", permitir la ejecución de la función y mostrar
        un mensaje indicando que el acceso fue permitido en el entorno de
        producción.
    3. Si el entorno no es "producción", evitar la ejecución de la función y mostrar
        un mensaje indicando que el acceso está restringido a entornos de
        producción.
        
Luego, aplica este decorador a dos funciones, subir_documento y
eliminar_documento. 

Intenta ejecutar estas funciones con diferentes entornos y
observa el comportamiento del decorador.
"""
def verificar_acceso_entorno(function):
    def wrapper(*args, **kargs):
        entorno = obtener_entorno()
        if entorno == "production":
            print("Acceso permitido en el entorno de producción.")
            return function(*args, **kargs)
        else: 
            print(f"Acceso restrigido a entornos de desarrollo a {function.__name__}.")
    return wrapper


@verificar_acceso_entorno
def subir_documento(documento):
    print(f"    · Subiendo documento: {documento}")


@verificar_acceso_entorno
def eliminar_documento(documento):
    print(f"    · Eliminando documento: {documento}")
    

# Entorno de producción
def obtener_entorno():
    return "production"

print(" · Entorno de PRODUCCION.")
subir_documento("Documento A")
eliminar_documento("Documento B")

print("·"*45)

# Entorno de desarrollo.
def obtener_entorno():
    return "desarrollo"

print(" · Entorno de DESARROLLO.")
subir_documento("Documento A")
eliminar_documento("Documento B")
