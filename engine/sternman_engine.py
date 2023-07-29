from abc import ABC

from car import Engine


class SternmanEngine(Engine, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on
        self.last_service_date=last_service_date

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
