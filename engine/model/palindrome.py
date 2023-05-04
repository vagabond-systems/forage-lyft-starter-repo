from datetime import datetime

from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery

class Palindrome(SternmanEngine):
    def __init__(self, last_service_date, warning_light_is_on ):
        self.engine = SternmanEngine(warning_light_is_on)
        self.battery = SpindlerBattery(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        service_threshold_date = self.engine.last_service_date.replace(year=self.engine.last_service_date.year + 2)
        service_threshold_light = self.warning_light_is_on

        if service_threshold_date < datetime.today().date() or service_threshold_light:
            return True
        return False