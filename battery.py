from abc import ABC, abstractmethod
from service import Serviceable
from datetime import date

class Battery(Serviceable):
    
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class SpindleBattery(Battery):
    def __init__(self, current_date:date, last_service_date:date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        
        if service_threshold_date < self.current_date:
            return True
        else:
            return False

class NubbinBattery(Battery):
    def __init__(self, current_date:date, last_service_date:date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        
        if service_threshold_date < self.current_date:
            return True
        else:
            return False