from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self, last_service_mileage=0, current_mileage=0):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    @abstractmethod
    def needs_service(self):
        pass
