from engine import Engine
from battery import Battery
from model.serviceable import Serviceable
from tire import Tire

class Car(Serviceable): 
    def __init__(self, car_engine: Engine, car_battery: Battery, car_tire: Tire) -> None:
        self.engine = car_engine
        self.battery = car_battery
        self.tire = car_tire

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()