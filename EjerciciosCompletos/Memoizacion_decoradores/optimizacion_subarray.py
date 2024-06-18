#Problema de Optimización de Subarreglo
"""
Imagina que estás trabajando en un sistema de análisis de datos y te han
proporcionado una lista de números enteros. 

Tu tarea es desarrollar una función llamada max_subarray_sum que encuentre 
y devuelva la suma máxima de un subarreglo contiguo en la lista.

Por ejemplo, considera la lista [1, -2, 3, 10, -4, 7, 2, -5] . 
El subarreglo contiguo con la suma máxima es [3, 10, -4, 7, 2] , 
y la suma de esos elementos es 18 . 
Por lo tanto, la función debería devolver 18 para esta lista.

Implementa la función max_subarray_sum y, además, aplica memoización para
mejorar su eficiencia en el cálculo de subarreglos de suma máxima en listas
previamente procesadas.

Explicación algoritmo de Kadane al final.
"""
## Cache implícito. Uso de functools

import functools

# Decorador para memorizar resultados y optimizar rendimiento en llamadas repetidas
@functools.lru_cache(maxsize=None)
def max_subarray_sum(arr):
    # Si el array está vacío, retorna 0 ya que no hay subarrays que evaluar
    if not arr:
        return 0
    
    # Inicializa la suma actual y la suma máxima con el primer elemento del array
    current_sum = max_sum = arr[0]
    # Inicializa el subarray con el primer elemento del array
    max_subarray= [arr[0]]
    
    # Itera sobre los elementos del array a partir del segundo elemento
    for num in arr[1:]:
        # Si el número actual es mayor que la suma del número actual y la suma actual
        if num > current_sum + num:
            # Reinicia la suma actual con el número actual
            current_sum = num
            # Reinicia el subarray con el número actual
            max_subarray = [num]
        else:
            # Añade el número actual a la suma actual
            current_sum+=num
            # Añade el número actual al subarray
            max_subarray.append(num)
        
        # Actualiza la suma máxima si la suma actual es mayor
        max_sum = max(max_sum, current_sum)
        
    # Retorna la suma máxima y el subarray contiguo que produce esa suma
    return max_sum, max_subarray

print("·"*60)
array = tuple([1, -2, 3, 10, -4, 7, 2, -5])        
resultado, subarray = max_subarray_sum(array)
print(f"Suma máxima del subarray contiguo es de: {resultado}")
print(f"Subarray contiguo con la suma maxima es: {subarray}")

print("·"*60)

array = tuple([2, -3, 5, 7, -1, 4, -2, 1])        
resultado, subarray = max_subarray_sum(array)
print(f"Suma máxima del subarray contiguo es de: {resultado}")
print(f"Subarray contiguo con la suma maxima es: {subarray}")

print("·"*60)

array = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])        
resultado, subarray = max_subarray_sum(array)
print(f"Suma máxima del subarray contiguo es de: {resultado}")
print(f"Subarray contiguo con la suma maxima es: {subarray}")

print("·"*60)

array = tuple([2, -3, 2, 2, 0])        
resultado, subarray = max_subarray_sum(array)
print(f"Suma máxima del subarray contiguo es de: {resultado}")
print(f"Subarray contiguo con la suma maxima es: {subarray}")



"""
El Algoritmo de Kadane es una técnica utilizada para encontrar la suma máxima 
de un subarreglo contiguo dentro de una matriz unidimensional (también conocida 
como vector o arreglo). Fue propuesto por el matemático estadounidense 
Joseph Born Kadane y se destaca por su eficiencia, ya que se ejecuta en tiempo 
lineal (O(n)).

Aquí está cómo funciona el algoritmo paso a paso:

Inicialización:
    Comenzamos con dos variables:
        max_ending_here: Almacena la suma máxima de un subarreglo que termina en 
        la posición actual.
        max_so_far: Almacena la suma máxima de un subarreglo encontrado hasta el 
        momento.
    Ambas variables se inicializan con el primer elemento de la matriz.
    
Recorrido de la matriz:
    Para cada elemento en la matriz (a partir del segundo elemento):
        Calculamos la suma máxima de un subarreglo que termina en la posición actual:
            Si max_ending_here + elemento_actual es mayor que el propio elemento_actual, 
                actualizamos max_ending_here con esa suma.
            De lo contrario, reiniciamos max_ending_here con el valor del elemento_actual.
            
    Comparamos max_ending_here con max_so_far y actualizamos max_so_far si es mayor.
    
Resultado:
    Al final del recorrido, max_so_far contendrá la suma máxima del subarreglo contiguo.
"""