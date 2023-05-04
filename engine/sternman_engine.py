from abc import ABC

from car import Car


class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = bool(warning_light_is_on)

    def engine_needs_to_be_serviced(self):
        if self.warning_light_is_on:
            return True
        return False
