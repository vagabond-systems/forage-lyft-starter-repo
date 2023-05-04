from abc import ABC

from car import Car


class NubbinBattery(Car, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date
        self.last_service_date = last_service_date
        
    def battery_needs_to_be_serviced(self):
        needs_service = bool(self.current_date - self.last_service_date > 365 * 4)
        return needs_service