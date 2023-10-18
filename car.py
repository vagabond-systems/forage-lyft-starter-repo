from abc import ABC, abstractmethod
from serviceable import Serviceable

class Car:
    def __init__(self, engine: Serviceable, battery: Serviceable):
        self.engine = engine
        self.battery = battery
    
    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
    