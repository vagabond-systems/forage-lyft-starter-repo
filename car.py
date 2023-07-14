from abc import ABC
from serviceable import Serviceable

class Car(ABC,Serviceable):
    def __init__(self, engine,battery,tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service():
            return True
        else:
            return False

