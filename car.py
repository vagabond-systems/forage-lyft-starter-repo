from Serviceable import Serviceable
from engine.engine import Engine
from battery.battery import Battery
from tires.tires import Tires


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tires):
           self._engine = engine
           self._battery = battery
           self._tire = tire
           

    def need_service(self):
       return self._engine.need_service() or self._battery.need_service() or self._tire.need_service()
        
        