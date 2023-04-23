from abc import ABC, abstractmethod
from engine.engine import Engine

from serviceable.serviceable import Serviceable
from battery.battery import Battery


class Car(Serviceable, ABC):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery
        
    def needs_service(self) -> bool:
        print('is this happening')
        print (self.battery.needs_service())
        print(self.engine.needs_service())
        return self.battery.needs_service() or self.engine.needs_service()