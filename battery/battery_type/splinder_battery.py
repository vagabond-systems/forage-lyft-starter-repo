from abc import ABC

from battery import Battery


class SplinderBattery(Battery, ABC):
    def __init__(self, curr_date, last_serv_date):
        self.current_date = curr_date
        self.last_service_date = last_serv_date

    def needs_service(self):
         service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2) 
         return service_threshold_date < self.current_date
