from abc import ABC

from engine.engine import Engine


class WilloughbyEngine(Engine, ABC):
    def __init__(self, current_mileage, last_service_mileage):
        super().__init__(last_service_mileage,current_mileage)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
