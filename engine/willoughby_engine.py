from abc import ABC

from car import Car


class WilloughbyEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = int(current_mileage)
        self.last_service_mileage = int(last_service_mileage)

    def needs_service(self):
        needs_servicing = bool(self.current_mileage - self.last_service_mileage > 60000)
        return needs_servicing