from engine.Engine import Engine
from battery.Battery import Battery
from tire.Tire import Tire
from serviceable.Serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        return self.engine.needs_service and self.battery.needs_service and self.tire.needs_service()