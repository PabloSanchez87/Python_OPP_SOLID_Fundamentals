## Encapsulación : principio de ocultar detalles internos de un objeto y controlar el acceso.
    # Atributos públicos
    # Atributos privados (se definen con doble guión bajo__ )
    # Atributos protegidos ( indica que no debe ser accedido pero no se impide.)

# Atributos privados
print("\nAtributo privado:")
class Ejemplo:
    def __init__(self):
        self.__atributo_privado = "Pablo"
        self.__contraseña = 12345

    def get_atributo(self):
        print(f"El nombre puede ser Laura o {self.__atributo_privado.upper()}")
        print(f"Su contraseña es {self.__contraseña*3}")

valor = Ejemplo()
## print(valor.__atributo_privado) --> No se permite el acceso.
valor.get_atributo() # Sería un GET --> CONTROLAMOS LA FORMA DE ACCESO.
                     # "Podemos controlar como mostrar los valores (ej. Encriptados.)"

#######################################################################################
# OJO #
print(" --> OJO, realmente podría acceder al atributo privado: 'valor._Ejemplo__atributo_privado' ",valor._Ejemplo__atributo_privado)
valor._Ejemplo__atributo_privado = "Ha sido Hackeado."
print(" --> OJO,tmb podría modificar al atributo privado: 'valor._Ejemplo__atributo_privado' ",valor._Ejemplo__atributo_privado)
#######################################################################################

# Atributos protegidos. --> Se indica iniciando con un guión bajo inicial.
print("\nAtributo protegido:")

class Ejemplo2:
    def __init__(self):
        self._atributo_protegido = "Pablo"
        self._contraseña_protegida = 12345

    def get_atributo(self):
        print(f"El nombre puede ser Laura o {self._atributo_protegido.upper()}")
        print(f"Su contraseña es {self._contraseña_protegida*3}")

valor2 = Ejemplo2()
print(valor2._atributo_protegido) #--> Se puede lograr, pero no es la manera correcta.
valor2.get_atributo() # Sería un GET --> CONTROLAMOS LA FORMA DE ACCESO.
                     # "Podemos controlar como mostrar los valores (ej. Encriptados.)"



""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""  EJEMPLO GENÉRICO PARA UNA CUENTA BANCARIA """
""""""""""""""""""""""""""""""""""""""""""""""""""""""
print("\nEJEMPLO GENÉRICO PARA UNA CUENTA BANCARIA")
class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo) :
        self._numero_cuenta = numero_cuenta # protegido
        self.__saldo = saldo # privado

    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, monto):
        self.__saldo += monto
    
    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
        else:   
            print("Saldo insuficiente")


# Caso de uso.

cuenta = CuentaBancaria("123456", 1000)
print(f"\tNumero de cuenta: {cuenta._numero_cuenta}")
print(f"\tSaldo: {cuenta.get_saldo()}")
cuenta.depositar(1000)
cuenta.retirar(500)
print("Después de movimientos.")
print(f"\tNumero de cuenta: {cuenta._numero_cuenta}")
print(f"\tSaldo: {cuenta.get_saldo()}")


""""""""""""""""""""""""""""""""""""""
"""  EJEMPLO SETTERS Y GETTERS """
""""""""""""""""""""""""""""""""""""""
print("\nEJEMPLO SETTERS Y GETTERS")
class Ejemplo3:
    def __init__(self):
        self.__atributo_privado = 30

    def getter(self):
        return self.__atributo_privado
    
    def setter (self, valor):
        if valor > 0:
            self.__atributo_privado += valor
        else:
            print("El valor debe ser positivo.")

ejemplo = Ejemplo3()
print(ejemplo.getter())
ejemplo.setter(2)
print(ejemplo.getter())



