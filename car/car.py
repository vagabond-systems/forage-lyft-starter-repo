from car.serviceable import Serviceable
from engine.engine import Engine
from battery.battery import Battery


# car class that has an engine and battery
class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery) -> None:
        self.__battery = battery
        self.__engine = engine

    # returns true if engine or battery needs service
    def needs_service(self) -> bool:
        return self.__engine.needs_service() or self.__battery.needs_service()
