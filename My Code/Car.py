from Engine import *
from Battery import *

class Car:
    def __init__(self,
                current_date: date,
                last_service_date: date,
                current_mileage: int,
                last_service_mileage: int,
                engine: Engine,
                battery: Battery):
        self.engine = Engine(last_service_mileage: int, current_mileage: int)
        self.battery = Battery(last_service_date: date, current_date:date)
        # all the other attributes?

    def needs_service() -> bool:
        return self.engine.needs_service() or self.battery.needs_service()