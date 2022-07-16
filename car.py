from abc import ABC, abstractmethod

from django.template import engines

from Serviceable import Serviceable
from engine.engine import Engine
from Battery.battery import Battery


class Car(Serviceable, ABC):
    def __init__(self, engine: Engine, battery: Battery):
           self._engine = engine
           self._battery = battery
           
    def engine(self) -> Engine:
        return self._engine
    
    def battery(self) -> Battery:
        return self._battery
    
    @abstractmethod
    def need_service(self):
       return self._engine.need_service() and self._battery.need_service()
        
        