from .serviceable_interface import Serviceable
from car_module.car_components.battery.battery_interface import Battery
from car_module.car_components.engine.engine_interface import Engine


class Car(Serviceable):
    def __init__(self, engine:Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) ->bool:
        return self.engine.needs_service() or self.battery.needs_service()
