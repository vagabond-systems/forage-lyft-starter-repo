from abc import ABC

from car import Engine,Battery


class CapuletEngine(Engine,ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.last_service_date =last_service_date
        self.mil =30000

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > self.mil
