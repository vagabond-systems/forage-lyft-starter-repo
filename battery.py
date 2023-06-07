from abc import ABC, abstractmethod

class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        # Logic to determine if Spindler battery needs service
        pass

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        # Logic to determine if Nubbin battery needs service
        pass
