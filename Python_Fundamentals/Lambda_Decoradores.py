# LAMBDA
# Funciones anonimas. Ayudan a abreviar y ahorrar tiempo.

def area_triangulo(base, altura):
    return (base*altura/2)
print(area_triangulo(5,7))
print(area_triangulo(9,6))

# Versión LAMBDA
area = lambda base, altura:(base*altura/2)
print(area(5,7))
print(area(9,6))

# Ejemplo Potencia
al_cubo =  lambda numero:numero**3
print(al_cubo(3))

# Ejemplo de formateo
destacar_valor = lambda comision: f"¡{comision}! $"
print(destacar_valor(1000))

# Ejemplo: Filtro.
numbers = [1,2,3,4,5,7]
def number_even(number):
    if number % 2 == 0:
        return True
print(list(filter(number_even, numbers)))

print(list(filter(lambda number_even: number_even % 2 == 0, numbers)))

# Ejemplo: uso lambda como clave
autores = ["Pablo Sánchez", "David Carrillo", "Laura Asorey"]
autores.sort()
print(autores)
# vamos a ordenar por apellidos, pasándole una key=lambda
autores.sort(key=lambda name:name.split(" ")[-1])
print(autores)

### DECORADORES ###
# Son funciones que añaden un funcionalidad a funciones ya existentes en nuestro programa
# Estructura:
# 3 funciones(A,B,C) donde A recibe como parámetro la función B y devuelve C
# Un decorador devuelve una función.
def funcion_decorador(funcion):
    def funcion_interna():
        pass
        # Código de funcion interna
    return (funcion_interna)


# Ejemplos ilustrativos.
def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        # Acciones adicionales que decoran
        print("Vamos a realizar una calculo:", end=" ")
    
        funcion_parametro()

        print("Hemos terminado el calculo.")
    return (funcion_interior)

@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(10-3)

suma()
resta()

# Sobreescribo. Usamos *args.
def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        # Acciones adicionales que decoran
        print("Vamos a realizar una calculo:", end=" ")
    
        funcion_parametro(*args)

        print("Hemos terminado el calculo.")
    return (funcion_interior)


@funcion_decoradora
def suma(num1,num2,num3):
    print(num1+num2+num3)

@funcion_decoradora
def resta(num1,num2):
    print(num1-num2)

suma(7,3,2)
resta(10,2)


# Sobreescribo. Usamos **kwargs para tener parametros de palabra-clave. KEYWORDS ARGUMENTS.
def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs):
        # Acciones adicionales que decoran
        print("Vamos a realizar una calculo:", end=" ")
    
        funcion_parametro(*args, **kwargs)

        print("Hemos terminado el calculo.")
    return (funcion_interior)


@funcion_decoradora
def potencia(base, exponente):
    print(base**exponente)

potencia(base=4, exponente=2)