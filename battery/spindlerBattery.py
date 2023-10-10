from abc import ABC
from battery import Battery
from datetime import datetime

class SpindlerBattery(Battery, ABC):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.batteryServiceYears = 2

    def needs_service(self):
        if self.last_service_date - self.current_date < self.batteryServiceYears:
            return True
        else:
            return False