# Código acoplado
print("·"*35)
print(" ·· Acoplado ..")
class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name: str, quantity: int, price: float) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

# No debería pertenecer a la clase Order.
    def total_price(self):
        total = 0
        for quantity, price in zip(self.quantities, self.prices):
            total += quantity * price
        return total

# Tampoco el método de pagar.
    def pay(self, payment_type: str, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
order.pay("debit", "0372846")


## Código SOLID - Refactorizado.
print("·"*35)
print(" ·· Refactorizado ..")

class Order:
    def __init__(self) -> None:
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"
        
    def add_item(self, name:str, quantity:int, price:float) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
    
        
class PaymentProcesor:
    def pay(self, order:Order, security_code:str, payment_type:str):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            order.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            order.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")


class CalculateProcesor:
    def total_price(self, order:Order):
        total = 0
        for quantity, price in zip(order.quantities, order.prices):
            total += quantity * price
        return total

if __name__ == "__main__":
    order = Order()
    
    print(order.status)
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)
    
    procesor = PaymentProcesor()
    procesor.pay(order, "12345", "debit")
    print(order.status)
    
    total= CalculateProcesor()
    print(f"Coste total: {total.total_price(order)}")