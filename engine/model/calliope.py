from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.Battery.spindler import SpindlerBattery


class Calliope(CapuletEngine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.last_service_date =last_service_date
        self.batteryClass=SpindlerBattery(last_service_date =self.last_service_date)
        self.engineClass = CapuletEngine(last_service_date=self.last_service_date,current_mileage=self.current_mileage,last_service_mileage=self.last_service_mileage)
    pass
    # def needs_service(self):
    #     service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
    #     if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
    #         return True
    #     else:
    #         return False
