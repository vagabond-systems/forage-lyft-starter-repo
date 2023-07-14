from engine import Engine
from battery import Battery
from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self._engine = engine
        self._battery = battery

