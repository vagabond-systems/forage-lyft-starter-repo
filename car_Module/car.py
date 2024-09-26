#import necessary libraries
from .serviceable_Interface import Serviceable
from .components.battery.battery_Interface import Battery
from .components.engine.engine_Interface import Engine

#Car class object with engine/battery and service status 
class Car(Serviceable):
    def __init__(self, engine:Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()