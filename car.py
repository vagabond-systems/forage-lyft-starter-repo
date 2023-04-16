from engine.Engine import Engine
from battery.Battery import Battery
from serviceable.Serviceable import Serviceable
from tire.tire import Tire


class Car(Serviceable):
    def __init__(self, engine_type, battery_type, tire_type):
        self.engine = engine_type
        self.battery = battery_type
        self.tire = tire_type

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.need_service()
