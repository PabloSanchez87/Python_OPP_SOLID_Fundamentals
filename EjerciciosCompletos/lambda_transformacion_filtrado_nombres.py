# Problema de Transformación y Filtrado de Nombres
"""
Imagina que te encuentras desarrollando una herramienta de procesamiento de
nombres para una aplicación de gestión de contactos. 
Tienes una lista de nombres en el formato "Apellido, Nombre", 
realiza las siguientes tareas:
    1. Utiliza la función lambda para transformar una lista de nombres completos
        al nuevo formato.
    2. Filtra la lista para incluir solo los nombres que contienen al menos dos
        vocales y tienen una longitud mayor a 10 caracteres.

Entrada: ["Pérez,Juan", "López, María"]]
Salida filtrada: ["María López", "José García"]
"""

lista_nombres = ["Pérez,Juan", "López,María", 
                 "García,José", "Martín,Ana",
                 "Lea,Kho","Zerrano,Xavier", 
                 "Mo,Chn"
                 ]

def transformar_lista(lista_nombres):
    lista_nombres_transformados = [(lambda nombre_original:
                                        nombre_original.split(",")[1]+" "+nombre_original.split(",")[0])
                                            (nombre_original) for nombre_original in lista_nombres]

    return lista_nombres_transformados


def filtrar_nombres(lista_nombres_transformados):
    # función interna.
    def nombre_valido(nombre):
        vocales= "aeiouáéíóúAEIOUÁÉÍÓÚ"
        return sum(1 for letra in nombre if letra in vocales)>=2 and len(nombre) > 10
    
    return [nombre for nombre in lista_nombres_transformados if nombre_valido(nombre)]


def nombres_no_aceptados(lista_transformada, lista_filtrada):
    return [nombre for nombre in lista_transformada if nombre not in lista_filtrada]


def razonar_exclusion_nombres(lista_no_aceptados):
    razones = {}
    for nombre in lista_no_aceptados:
        vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
        num_vocales = sum(1 for letra in nombre if letra in vocales)
        if num_vocales < 2:
            razones[nombre] = "No tiene al menos dos vocales."
        elif len(nombre) <= 10:
            razones[nombre] = "La longitud es igual o menor a 10 caracteres."
        else:
            razones[nombre] = "Otra razón no especificada."
    return razones



# Ejecución principal. 
print("·"*40)
lista_transformada = transformar_lista(lista_nombres)
print(f"Lista transformada: {lista_transformada}")
print("·"*40)

lista_filtrada = filtrar_nombres(lista_transformada)
print(f"Lista filtrada: {lista_filtrada}")
print("·"*40)

lista_no_aceptados = nombres_no_aceptados(lista_transformada, lista_filtrada)
print(f"Lista no aceptados: {lista_no_aceptados}")
print("·"*40)

razones = razonar_exclusion_nombres(lista_no_aceptados)
for nombre, razon in razones.items():
    print(f"Nombre: {nombre} - Razón: {razon}")
print("·"*40)