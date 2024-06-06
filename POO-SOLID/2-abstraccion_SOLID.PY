class Vehiculo:
    def __init__(self,marca, modelo) :
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.velocidad = 0

    def mostrar_vehiculo(self):
        print(f"Marca: {self.marca}, modelo: {self.modelo}")
        print(f"  Encendido: {self.encendido}, Velocidad: {self.velocidad} km/h")

    def encender(self):
        self.encendido = True
        print("El vehículo está encendido.")

    def apagar(self):
        self.encendido = False
        print("El vehículo está apagado.")

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            print(f"El vehículo acelerado hasta los : {self.velocidad} km/h.")
        else:
            print("No se puede acelerar. Encienda el vehículo.")

    def frenar(self, decremento):
        if self.encendido:
            if self.velocidad - decremento >=0:
                self.velocidad -= decremento
                print(f"El vehículo ha desacelerado has los: {self.velocidad} km/h.")
            else: 
                self.velocidad = 0
                print("El vehículo se ha parado.")
        else:
            print(f"No se puede frenar un vehículo ya parado.")

vehiculo1 = Vehiculo("Mercedes", "GLA220d")
vehiculo1.mostrar_vehiculo()
vehiculo1.encender()
vehiculo1.acelerar(20)
vehiculo1.frenar(20)
vehiculo1.apagar()



        