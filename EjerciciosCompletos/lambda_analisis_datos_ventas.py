# Problema de Análisis de Datos de Ventas

"""
Imagina que eres parte de una empresa de comercio electrónico y tienes
información detallada sobre las ventas de productos. 

Cada venta se representa como un diccionario, que incluye:
    - el nombre del producto, 
    - la fecha de venta, 
    - el monto de la venta y 
    - la ubicación del comprador. 

Realiza un análisis avanzado de estas ventas.
    1. Filtra las ventas realizadas en el último trimestre del año.
    2. Selecciona solo las ventas de productos con un monto superior a $500.
    3. Agrupa las ventas por ubicación del comprador.
    4. Calcula el promedio del monto de venta para cada ubicación.
    5. Ordena las ubicaciones por el promedio del monto de venta de forma descendente. 

Utiliza funciones lambda.
"""
from datetime import datetime

ventas = [
    {"nombre_producto":"iphone13", "fecha_venta":"2023-10-01", "coste": 1000, "ubicacion":"España"},
    {"nombre_producto":"MacBook Pro", "fecha_venta":"2023-11-01", "coste": 2000, "ubicacion":"USA"},
    {"nombre_producto":"SG12", "fecha_venta":"2023-12-01", "coste": 500, "ubicacion":"England"},
    {"nombre_producto":"SG12", "fecha_venta":"2024-02-11", "coste": 400, "ubicacion":"España"},
    {"nombre_producto":"iphone14", "fecha_venta":"2023-09-15", "coste": 1100, "ubicacion":"Canada"},
    {"nombre_producto":"MacBook Air", "fecha_venta":"2023-10-20", "coste": 1500, "ubicacion":"USA"},
    {"nombre_producto":"Pixel 6", "fecha_venta":"2023-11-05", "coste": 700, "ubicacion":"Australia"},
    {"nombre_producto":"iphone13", "fecha_venta":"2023-12-11", "coste": 950, "ubicacion":"España"},
    {"nombre_producto":"Galaxy S21", "fecha_venta":"2023-09-25", "coste": 800, "ubicacion":"South Korea"},
    {"nombre_producto":"Surface Pro", "fecha_venta":"2024-01-15", "coste": 1200, "ubicacion":"USA"},
    {"nombre_producto":"iphone14", "fecha_venta":"2024-03-01", "coste": 1150, "ubicacion":"England"},
    {"nombre_producto":"SG12", "fecha_venta":"2024-04-10", "coste": 450, "ubicacion":"Spain"},
    {"nombre_producto":"Pixel 7", "fecha_venta":"2023-08-30", "coste": 750, "ubicacion":"Canada"},
    {"nombre_producto":"MacBook Pro", "fecha_venta":"2023-11-18", "coste": 2100, "ubicacion":"Germany"},
    {"nombre_producto":"Galaxy S21", "fecha_venta":"2023-10-10", "coste": 850, "ubicacion":"France"},
    {"nombre_producto":"iphone13", "fecha_venta":"2024-02-22", "coste": 980, "ubicacion":"Italy"},
    {"nombre_producto":"Surface Pro", "fecha_venta":"2024-03-15", "coste": 1250, "ubicacion":"Netherlands"},
    {"nombre_producto":"MacBook Air", "fecha_venta":"2023-12-02", "coste": 1550, "ubicacion":"Japan"},
    {"nombre_producto":"Pixel 6", "fecha_venta":"2023-11-22", "coste": 720, "ubicacion":"Brazil"},
    {"nombre_producto":"iphone14", "fecha_venta":"2024-01-05", "coste": 1120, "ubicacion":"Mexico"}
]


def analizar_ventas(ventas):
    # 1. Filtra las ventas realizadas en el último trimestre del año.
    ventas_filtradas = [venta for venta in ventas if datetime.strptime(venta["fecha_venta"], "%Y-%m-%d").month>=10]    
    
    # 2. Selecciona solo las ventas de productos con un monto superior a $500.
    ventas_filtradas = [venta for venta in ventas_filtradas if venta["coste"]>500]
    
    # 3. Agrupa las ventas por ubicación del comprador.
    ventas_agrupadas = {}
    for venta in ventas_filtradas:
        ubicacion = venta["ubicacion"]
        if ubicacion not in ventas_agrupadas:
            ventas_agrupadas[ubicacion] = []
        ventas_agrupadas[ubicacion].append(venta)
    
    # 4. Calcula el promedio del monto de venta para cada ubicación.
    promedio_ventas = {}
    for ubicacion in ventas_agrupadas:
        ventas_por_ubicacion = ventas_agrupadas[ubicacion]
        promedio_ventas[ubicacion]=sum(venta["coste"] for venta in ventas_por_ubicacion)/len(ventas_por_ubicacion)
        
    # 5. Ordena las ubicaciones por el promedio del monto de venta de forma descendente.     
    ubicaciones_ordenadas = sorted(promedio_ventas, 
                                   key=lambda ubicacion:promedio_ventas[ubicacion], 
                                            reverse=True)
    for ubicacion in ubicaciones_ordenadas:
        print(f"    · {ubicacion}: {promedio_ventas[ubicacion]} €")
    
print("·"*30)
analizar_ventas(ventas)
print("·"*30)

########################################################################################################################

## Versión usando from collections import defaultdict
from collections import defaultdict

def analizar_ventas2(ventas):
    # 1. Filtra las ventas realizadas en el último trimestre del año.
    ventas_filtradas = [venta for venta in ventas if datetime.strptime(venta["fecha_venta"], "%Y-%m-%d").month in [10, 11, 12]]    
    
    # 2. Selecciona solo las ventas de productos con un monto superior a $500.
    ventas_filtradas = [venta for venta in ventas_filtradas if venta["coste"] > 500]
    
    # 3. Agrupa las ventas por ubicación del comprador.
    ventas_agrupadas = defaultdict(list)
    for venta in ventas_filtradas:
        ventas_agrupadas[venta["ubicacion"]].append(venta["coste"])
    
    # 4. Calcula el promedio del monto de venta para cada ubicación.
    promedio_ventas = {ubicacion: sum(costes) / len(costes) for ubicacion, costes in ventas_agrupadas.items()}
        
    # 5. Ordena las ubicaciones por el promedio del monto de venta de forma descendente.     
    ubicaciones_ordenadas = sorted(promedio_ventas.items(), key=lambda item: item[1], reverse=True)
    
    # Imprimir el resultado
    for ubicacion, promedio in ubicaciones_ordenadas:
        print(f"    · {ubicacion}: {promedio:} €")
    
print("·"*45)
print(" VERSIÓN: FORM COLLECTIONS IMPORT DEFAULTDICT")
print("·"*45)
analizar_ventas2(ventas)
print("·"*30)
