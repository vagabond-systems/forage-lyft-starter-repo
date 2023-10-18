from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from serviceable import Serviceable

class SpindlerBattery(Serviceable):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days >= (365 * 2)

class NubbinBattery(Serviceable):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days >= (365 * 4)
