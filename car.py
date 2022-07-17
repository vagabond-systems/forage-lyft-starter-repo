from Serviceable import Serviceable
from engine.engine import Engine
from Battery.battery import Battery


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
           self._engine = engine
           self._battery = battery
           

    def need_service(self):
       return self._engine.need_service() or self._battery.need_service()
        
        