from service import Serviceable
from battery import Battery
from engine import Engine

class Car(Serviceable):
    def __init__(self, Engine, Battery):
        self.engine = Engine
        self.battery = Battery

    def needs_service(self) -> bool:
        if(self.engine.needs_service() or self.battery.needs_service()):
            return True
        return False


