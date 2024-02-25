from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, warning_indicator):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_indicator = warning_indicator 


    @abstractmethod
    def needs_service(self):
        pass