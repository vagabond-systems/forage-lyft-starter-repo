from abc import ABC, abstractmethod
from datetime import datetime
from car import Car


class CapuletEngine(Car, ABC):
    SERVICE_INTERVAL = 30000

    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    @abstractmethod
    def requires_service(self):
        pass

    def requires_engine_service(self):
        return self.current_mileage - self.last_service_mileage > CapuletEngine.SERVICE_INTERVAL

    def requires_battery_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < datetime.today().date()

