# ABC -> abstract methods
from abc import ABC, abstractmethod

# Interface
class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass

    @abstractmethod
    def set_temperature(self, temperature: int) -> None:
        pass


# subclases -> implements INTERFACE
class SmartLight(

):
    def turn_off(self) -> None:
        print("Turning lights ON")

    def turn_on(self) -> None:
        print("Turning lights OFF")

    # THIS IS NOT INTERFACE SEGREFATION PRINCIPLE
    def set_temperature(self, temperature: int) -> None:
        raise NotImplementedError("Smart light device cannot set temperature")


class SmartTherm(

):
    def turn_off(self) -> None:
        print("Turning temperature OFF")

    def turn_on(self) -> None:
        print("Turning temperature ON")

    def set_temperature(self, temperature: int) -> None:
        print(f"Setting temperature {temperature}")


smartLight = SmartLight()
smartLight.turn_off()
smartLight.turn_on()
#smartLight.set_temperature(10)
smartTherm = SmartTherm()
smartTherm.turn_off()
smartTherm.turn_on()
smartTherm.set_temperature(10)