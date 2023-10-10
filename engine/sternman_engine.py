from abc import ABC
from engine import Engine 

class SternmanEngine(Engine, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.isWarningLightOn = False

    def needs_service(self):
        if self.isWarningLightOn == True:
            return True
        else:
            return False
