# using PROTOCOL
from typing import Protocol

class IOperacionFinanciera(Protocol):
    def depositar(self, monto: float) -> None: ...
    def retirar(self, monto: float) -> None: ...
    def transferir(self, monto: float, a_cuenta: str) -> None: ...

# Con PROTOCOL no nos obliga a indicarle que vamos a implementar
# la interfaz, al llamar a un método ya sabe que lo vas a hacer. 
class CuentaAhorros:
    def depositar(self, monto: float) -> None:
        print(f"Depositando { monto} en cuenta de ahorros")

    def retirar(self, amount: float) -> None:
        print(f"Retirando {amount} de cuenta de ahorros")
        
        
        # Raise una excepcion rompe ISP
    def transferir(self, monto: float, a_cuenta: str) -> None:
        raise NotImplementedError("No se puede transferir.")


class CuentaCorriente:
    def depositar(self, monto: float) -> None:
        print(f"Depositando { monto} en cuenta corriente")

    def retirar(self, amount: float) -> None:
        print(f"Retirando {amount} de cuenta corriente")

    def transferir(self, amount: float, a_cuenta: str) -> None:
        print(f"Transfiriendo {amount} de cuenta corriente a cuenta { a_cuenta}")



cuentaAhorros = CuentaAhorros()
cuentaAhorros.depositar(100)
cuentaAhorros.retirar(50)
try:
    cuentaAhorros.transferir(20, "ABCSK189148")
except NotImplementedError as e:
    print(e)

cuentaCorriente = CuentaCorriente()
cuentaCorriente.depositar(100)
cuentaCorriente.retirar(50)
cuentaCorriente.transferir(20, "ABCSK189148")