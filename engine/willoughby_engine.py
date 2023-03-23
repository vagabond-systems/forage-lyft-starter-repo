from abc import ABC, abstractmethod
from car import Car


class WilloughbyEngine(Car, ABC):
    SERVICE_INTERVAL = 60000

    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    @abstractmethod
    def requires_service(self):
        pass

    def requires_engine_service(self):
        return self.current_mileage - self.last_service_mileage > WilloughbyEngine.SERVICE_INTERVAL

