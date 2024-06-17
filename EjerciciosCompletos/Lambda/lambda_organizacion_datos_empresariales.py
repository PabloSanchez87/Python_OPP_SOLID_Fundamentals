# Problema de Organización de Datos Empresariales:

"""
Imagina que trabajas en una empresa internacional con equipos distribuidos en
diferentes países. Cada equipo tiene una lista de empleados, representados
como diccionarios, con información sobre el nombre, la edad y el rendimiento
en proyectos recientes.

Tu tarea es organizar una lista consolidada de todos los empleados de la
empresa. 

La organización debe seguir ciertas reglas:
    1. Los empleados se deben ordenar por el rendimiento en proyectos recientes
        de forma descendente.
    2. Para aquellos con el mismo rendimiento, se deben ordenar por edad de
        forma ascendente. Además, deseas agrupar a los empleados por país para
        un análisis más efectivo. Utiliza funciones lambda.
"""

from itertools import groupby

def ordenar_empleados(empleados):
    # Ordenar primero por rendimiento descendente y luego por edad ascendente
    empleados_ordenados = sorted(empleados, key=lambda empleado: 
                                (empleado['rendimiento'], -empleado['edad']),
                                reverse=True)
    print("·"*40)
    print(" . Empleados ordenados:")
    for empleado in empleados_ordenados:
        print(empleado)
    print("·"*40)
    return empleados_ordenados
    
    
def agrupar_empleados_por_pais(empleados_ordenados):
    # Asegurarse de que están ordenados por país para el groupby
    empleados_ordenados_por_pais = sorted(empleados_ordenados, key=lambda empleado: empleado['pais'])
    empleados_agrupados = {pais : list(grupo_empleados) 
                           for pais, grupo_empleados in 
                                groupby(empleados_ordenados_por_pais, 
                                        key= lambda empleado:empleado['pais'])}
    return empleados_agrupados


def mostrar_empleados_agrupados(empleados_agrupados):
    for pais, grupo_empleados in empleados_agrupados.items():
        print(f"\nPais: {pais}")
        for empleado in grupo_empleados:
            print(empleado)
            

empleados = [
    {"nombre": "Juan Perez", "edad":30, "pais": "España", "rendimiento": 90}, 
    {"nombre": "Maria Garcia", "edad":28, "pais": "España", "rendimiento": 85}, 
    {"nombre": "Pedro Rodriguez", "edad":26, "pais": "Argentina", "rendimiento": 95}, 
    {"nombre": "Ana Perez", "edad":32, "pais": "Argentina", "rendimiento": 100}, 
    {"nombre": "Jose Lopez", "edad":29, "pais": "Bolivia", "rendimiento": 95}, 
    {"nombre": "Ana Sanchez", "edad":35, "pais": "Bolivia", "rendimiento": 105}, 
]

empleados2 = [
    {"nombre": "Juan Pérez", "edad": 30, "pais": "España", "rendimiento": 90},
    {"nombre": "María García", "edad": 28, "pais": "España", "rendimiento": 85},
    {"nombre": "Pedro Rodríguez", "edad": 26, "pais": "Argentina", "rendimiento": 95},
    {"nombre": "Ana Rodríguez", "edad": 32, "pais": "Argentina", "rendimiento": 105},
    {"nombre": "Sofía Gómez", "edad": 29, "pais": "Argentina", "rendimiento": 95},
    {"nombre": "José López", "edad": 32, "pais": "Bolivia", "rendimiento": 80},
    {"nombre": "Ana Sánchez", "edad": 35, "pais": "Bolivia", "rendimiento": 85},

]
empleados_ordenaos = ordenar_empleados(empleados)
empleados_agrupados = agrupar_empleados_por_pais(empleados_ordenaos)
mostrar_empleados_agrupados(empleados_agrupados)
print("·"*40)
empleados_ordenaos = ordenar_empleados(empleados2)
empleados_agrupados = agrupar_empleados_por_pais(empleados_ordenaos)
mostrar_empleados_agrupados(empleados_agrupados)