import os
from engine.engine import Engine


class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self, val):
        self.current_mileage = val
        return self.current_mileage - self.last_service_mileage >= os.environ.get('CAPULET')

    def perform_service(self):
        self.last_service_mileage = self.current_mileage
