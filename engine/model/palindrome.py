from datetime import datetime

from engine.sternman_engine import SternmanEngine
from engine.Battery.Nubbin import NubbinBattery

class Palindrome(SternmanEngine):
    def __init__(self, last_service_date, warning_light_is_on):
        self.last_service_date =last_service_date
        self.warning_light_is_on = warning_light_is_on
        self.batteryClass=NubbinBattery(last_service_date =self.last_service_date)
        self.engineClass = SternmanEngine(last_service_date=self.last_service_date,warning_light_is_on=self.warning_light_is_on)

    # def needs_service(self):
    #     service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
    #     if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
    #         return True
    #     else:
    #         return False
