from datetime import datetime

from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery


class Thovex(CapuletEngine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine(last_service_mileage)
        self.battery = NubbinBattery(last_service_date)
        self.last_service_mileage = last_service_mileage
        self.current_milleage = current_mileage

    def needs_service(self):
        service_threshold_date = self.battery.last_service_date.replace(year=self.battery.last_service_date.year + 4)
        service_threshold_mileage = self.current_milleage - self.last_service_mileage >= 60000

        if service_threshold_date < datetime.today().date() or service_threshold_mileage:
            return True
        return False
