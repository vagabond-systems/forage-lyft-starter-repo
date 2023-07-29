from abc import ABC

from car import Battery
from datetime import datetime

class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = datetime.today().date()
        # self.threshold_year = threshold_year
        

    def engine_should_be_serviced(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False