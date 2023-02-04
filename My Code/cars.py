from engines import *
from batteries import *
from datetime import datetime, date

class Car:
    def __init__(self,
                current_date: date,
                last_service_date: date,
                current_mileage: int,
                last_service_mileage: int,
                engine: Engine,
                battery: Battery):
        self.engine = engine(last_service_mileage, current_mileage)
        self.battery = battery(last_service_date, current_date)

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()