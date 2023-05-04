from abc import ABC

from car import Car


class CapuletEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = int(current_mileage)
        self.last_service_mileage = int(last_service_mileage)

    def engine_needs_to_be_serviced(self):
        needs_service = bool(self.current_mileage - self.last_service_mileage > 30000)
        return needs_service