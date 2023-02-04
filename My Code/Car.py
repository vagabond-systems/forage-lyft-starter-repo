from Engine import *
from Battery import *

class Car:
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = Engine()
        self.battery = Battery()
        # all the other attributes?

    def needs_service() -> bool:
        return Engine.needs_service() or Battery.needs_service()