# Memoización en Costos de Envío.
"""
Imagina que estás trabajando en un sistema de gestión de costos de envío para
una empresa de logística. 
El sistema debe calcular el costo de envío para diferentes destinos, distancias
y pesos de paquetes. 
Implementa una función llamada calcular_costo_envio que tome como entrada un 
destino, una distancia en kilómetros y un peso en kilogramos, y devuelva el 
costo total del envío.

Requerimientos:
    1. El costo base de envío es de $5.0.
    2. El costo por kilómetro de distancia es de $0.1.
    3. El costo por kilogramo de peso es de $0.2.
    
Implementa la función de manera eficiente utilizando memoización para evitar
recalcular el costo para los mismos destinos, distancias y pesos.
"""
import functools
import time

# Constantes.
COSTE_BASE = 5.0
COSTE_KM = 0.1
COSTE_KG = 0.2

@functools.lru_cache(maxsize=None)
def calcular_costo_envio(destino, distancia, peso):
    coste_distancia = distancia * COSTE_KM
    coste_peso = peso * COSTE_KG
    # Calculamos el coste total.
    coste_total = COSTE_BASE + coste_distancia + coste_peso
    return coste_total

# Ejemplo de uso.
# SIN MEMOIZACION
inicio = time.time()
destino_1 = "Ciudad A"
distancia_1 = 150
peso_1 = 2.5
coste_sin_memoizacion_1 = calcular_costo_envio(destino_1, distancia_1, peso_1)
destino_2 = "Ciudad B"
distancia_2 = 100
peso_2 = 4.5
coste_sin_memoizacion_2 = calcular_costo_envio(destino_2, distancia_2, peso_2)
fin = time.time()
tiempo_total_1 = (fin-inicio)*1_000_000

# CON MEMOIZACION
inicio_2 = time.time()
destino_1 = "Ciudad A"
distancia_1 = 150
peso_1 = 2.5
coste_con_memoizacion_1 = calcular_costo_envio(destino_1, distancia_1, peso_1)
destino_2 = "Ciudad B"
distancia_2 = 100
peso_2 = 4.5
coste_con_memoizacion_2 = calcular_costo_envio(destino_2, distancia_2, peso_2)
fin_2= time.time()
tiempo_total_2 = (fin_2-inicio_2)*1_000_000

print("·"*60)
print(" · SIN MEMOIZACION · ")
print(f"Coste sin memoizacion para la {destino_1} es de: {coste_sin_memoizacion_1}")
print(f"Coste sin memoizacion para la {destino_2}  es de: {coste_sin_memoizacion_2}")
print(f"    · Tiempo sin memoizacion: {tiempo_total_1:.3f} nanosegundos.")
print("·"*60)
print(" · CON MEMOIZACION ·")
print(f"Coste con memoizacion para la {destino_1}  es de: {coste_con_memoizacion_1}")
print(f"Coste con memoizacion para la {destino_2}  es de: {coste_con_memoizacion_2}")
print(f"    · Tiempo con memoizacion: {tiempo_total_2:.3f} nanosegundos.")


