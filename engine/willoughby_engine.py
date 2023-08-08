from abc import ABC
from Car.serviceable import Serviceable 

class WilloughbyEngine(Serviceable, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        if self.current_mileage - self.last_service_mileage > 60000:
            return True
        else: 
            return False
