from abc import ABC
from car import Car


class SpinderBattery(Car,ABC):
     def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date
        
     def battery_should_be_serviced(self):
        return self.last_service_date - self.current_date > 3