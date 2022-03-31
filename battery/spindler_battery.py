from abc import ABC
from .battery import Battery

class SpindlerBattery(Battery, ABC):
    def __init__(self,last_service_date, current_date):
        self.last_service_date=last_service_date
        self.current_date = current_date