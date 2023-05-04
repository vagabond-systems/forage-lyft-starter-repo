from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery


class Glissade(WilloughbyEngine, SpindlerBattery):
    
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = WilloughbyEngine(last_service_mileage)
        self.battery = SpindlerBattery(last_service_date)
        self.last_service_mileage = last_service_mileage
        self.current_milleage = current_mileage

    def needs_service(self):
        service_threshold_date = self.engine.last_service_date.replace(year=self.engine.last_service_date.year + 2)
        service_threshold_mileage = self.current_milleage - self.last_service_mileage >= 30000

        if service_threshold_date < datetime.today().date() or service_threshold_mileage:
            return True
        return False