from engine import Engine
from battery import Battery
from model.serviceable import Serviceable

class Car(Serviceable): 
    def __init__(self, car_engine: Engine, car_battery: Battery) -> None:
        self.engine = car_engine
        self.battery =car_battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()