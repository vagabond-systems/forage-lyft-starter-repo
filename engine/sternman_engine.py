from abc import ABC, abstractmethod
from car import Car


class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    @abstractmethod
    def requires_service(self):
        pass

    def requires_engine_service(self):
        return self.warning_light_is_on

