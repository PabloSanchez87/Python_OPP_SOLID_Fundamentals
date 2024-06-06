"""
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
"""
## FECHAS
from datetime import datetime, date
import os


now = datetime.now()
print(f"Fecha actual--> {now}")

birth_date = datetime(1987,12,1,11,30,0)
print(f"Fecha de nacimiento --> {birth_date}")

diff = now - birth_date # Me devuelve la diferencia en días.
print(f"Tipo de dato de years: {type(diff)}")
print(f"Días --> {diff}")

print(f"Años --> {diff.days//365}") # Para calcular los años. Usamos la división entera para que me de los años exactos.

### EXTRA ###

## Formateo de fechas
# Día, mes y año
print(birth_date.strftime("%d-%m-%y")) 
print(birth_date.strftime("%d-%m-%Y")) # "%Y" me imprime año completo

# Horas, minutos y segundos
print(birth_date.strftime("%H-%M-%S")) # H M S en mayúsculas 

# Día del año
print(birth_date.strftime("%j"))  # j día del año

# Día de la semana
print(birth_date.strftime("%A")) # A - Día de la semana

# Nombre del mes
print(birth_date.strftime("%d-%h-%y")) # h - Abreviatura del mes
print(birth_date.strftime("%d-%B-%y")) # B - Mes completo

#Representación por defecto del locale
print(birth_date.strftime("%c"))  # Fecha y hora
print(birth_date.strftime("%x"))  # Fecha
print(birth_date.strftime("%X"))  # Horas minutos y segundos

# AM/PM
print(birth_date.strftime("%p")) 
