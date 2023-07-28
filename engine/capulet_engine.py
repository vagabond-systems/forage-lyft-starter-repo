from abc import ABC
from car import Serviceable

class CapuletEngine(Serviceable, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        """

        :rtype: object
        """
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
