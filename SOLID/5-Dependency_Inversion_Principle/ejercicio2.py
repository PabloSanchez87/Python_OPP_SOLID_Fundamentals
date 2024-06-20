from abc import ABC, abstractmethod

# Definir la ABSTRACCIÓN del servicio de almacenamiento de productos.
class AlmacenamientoProductos(ABC):
    @abstractmethod
    def agregar_producto(self, nombre:str, cantidad:int):
        pass
    
    @abstractmethod
    def obtener_stock(self, nombre:str) -> int:
        pass
    
# Implementacion del almacenamiento de productos
# Método de BAJO NIVEL --> detalles.
class MemoriaAlmacenamientoProductos(AlmacenamientoProductos):
    def __init__(self) -> None:
        self.inventario = {}
        
    def agregar_producto(self, nombre: str, cantidad: int):
        if nombre in self.inventario:
            self.inventario[nombre] += cantidad
        else:
            self.inventario[nombre] = cantidad
    
    def obtener_stock(self, nombre: str) -> int:
        return self.inventario.get(nombre, 0)
    
# Método de ALTO NIVEL - LÓGICA DE NEGOCIOS.
class GestorProductos:   
    def set_almacenamiento(self, almacenamiento: AlmacenamientoProductos): 
        self.almacenamiento = almacenamiento
        
    def agregar_producto(self, nombre: str, cantidad: int):
        self.almacenamiento.agregar_producto(nombre, cantidad)
        print(f"Producto {nombre} ha sido agregado al inventario.")
        
    def obtener_stock(self, nombre:str):
        stock = self.almacenamiento.obtener_stock(nombre)
        print(f"Stock de {nombre}: {stock} unidades.")
        return stock
    
    
# MODO DE USO
print("·"*40)
almacenamiento_memoria = MemoriaAlmacenamientoProductos()
gestor_productos = GestorProductos()
gestor_productos.set_almacenamiento(almacenamiento_memoria) ## inyección de dependencias.

gestor_productos.agregar_producto("Camisa", 2)
gestor_productos.agregar_producto("Pantalón", 5)
gestor_productos.agregar_producto("Gorro", 1)
gestor_productos.agregar_producto("Chaqueta", 3)
print("·"*40)
gestor_productos.obtener_stock("Camisa")
gestor_productos.obtener_stock("Pantalón")
gestor_productos.obtener_stock("Gorro")
gestor_productos.obtener_stock("Chaqueta")
print("·"*40)

