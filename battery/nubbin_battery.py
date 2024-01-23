from abc import ABC

from car import Car

from datetime import datetime

class NubbinBattery(Car, ABC):
    def __init__(self, last_service_date):
        self.service_threshold_date = last_service_date.replace(year=self.last_service_date.year + 4)

    def battery_should_be_serviced(self):
        return  self.service_threshold_date < datetime.today().date()
