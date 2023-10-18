from abc import ABC, abstractmethod
from serviceable import Serviceable
from datetime import datetime, timedelta

class CapuletEngine(Serviceable):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    
    def needs_service(self) -> bool:
        return (self.current_mileage - self.last_service_mileage) >= 30000

class WilloughbyEngine(Serviceable):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    
    def needs_service(self) -> bool:
        return (self.current_mileage - self.last_service_mileage) >= 60000

class SternmanEngine(Serviceable):
    def __init__(self, warning_light_on: bool):
        self.warning_light_on = warning_light_on
    
    def needs_service(self) -> bool:
        return self.warning_light_on