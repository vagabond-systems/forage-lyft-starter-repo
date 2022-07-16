from abc import ABC

from battery import Battery

class SplinderBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date) -> None:
        self.last_service_date =  last_service_date
        self.current_date = current_date
        
    def need_service(self):
        return True