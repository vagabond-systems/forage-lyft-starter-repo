from abc import ABC
from car import Car
from datetime import datetime

class CapuletEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        # Service criteria for CapuletEngine: Once every 30,000 miles
        return self.current_mileage - self.last_service_mileage > 30000
