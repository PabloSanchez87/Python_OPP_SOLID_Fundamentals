from typing import Protocol

# Contratos de deposito, retiro y transferencia
class IDepositar(Protocol):
    def depositar(self, monto: float) -> None: ...
class IRetirar(Protocol):
    def retirar(self, monto: float) -> None: ...
class ITransferir(Protocol):
    def transferir(self, monto: float) -> None: ...

# class CuentaAhorros: -> sería suficiente, no son necesarios los paréntesis
class CuentaAhorros(IDepositar, IRetirar):
    def depositar(self, monto: float) -> None:
        print(f"Depositando { monto} en cuenta de ahorros ")

    def retirar(self, amount: float) -> None:
        print(f"Retirando {amount} de cuenta de ahorros")

#class CuentaCorriente: -> sería suficiente, no son necesarios los paréntesis
class CuentaCorriente(IDepositar, IRetirar, ITransferir):
    def depositar(self, monto: float) -> None:
        print(f"Depositando { monto} en cuenta corriente")

    def retirar(self, amount: float) -> None:
        print(f"Retirando {amount} de cuenta corriente")

    def transferir(self, amount: float, a_cuenta: str) -> None:
        print(f"Transfiriendo {amount} de cuenta corriente a cuenta { a_cuenta}")


def realizar_pago(cuenta: ITransferir, monto: float) -> None:
    cuenta.transferir(monto, "ABCSK189148")

cuenta_ahorros = CuentaAhorros()
cuenta_corriente = CuentaCorriente()

cuenta_ahorros.depositar(100)
cuenta_ahorros.retirar(50)
cuenta_corriente.depositar(100)
cuenta_corriente.retirar(50)

realizar_pago(cuenta_corriente, 20)


