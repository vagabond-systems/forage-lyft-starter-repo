from abc import ABC, abstractmethod
from engine.engine import Engine

from serviceable.serviceable import Serviceable
from battery.battery import Battery
from tires.tires import Tires


class Car(Serviceable, ABC):
    def __init__(self, engine: Engine, battery: Battery, tires: Tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires
        
    def needs_service(self) -> bool:
        print('is this happening')
        # print (self.battery.needs_service())
        # print(self.engine.needs_service())
        print(self.tires)
        return self.battery.needs_service() or self.engine.needs_service() or self.tires.needs_service(self.tires.tire_wear)