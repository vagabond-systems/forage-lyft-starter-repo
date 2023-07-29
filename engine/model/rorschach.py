from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from engine.Battery.Nubbin import NubbinBattery



class Rorschach(WilloughbyEngine,NubbinBattery):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.last_service_date =last_service_date
        self.batteryClass=NubbinBattery(last_service_date =self.last_service_date)
        self.engineClass = WilloughbyEngine(last_service_date=self.last_service_date,current_mileage=self.current_mileage,last_service_mileage=self.last_service_mileage)
    # def needs_service(self):
        # service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        # if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
        #     return True
        # else:
        #     return False
