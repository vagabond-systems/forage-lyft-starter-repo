from abc import ABC
from car import Serviceable

class SternmanEngine(Serviceable, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        return self.warning_light_is_on
