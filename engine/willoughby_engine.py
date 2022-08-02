from abc import ABC, abstractmethod

from engine import Engine

class WilloughbyEngine(Engine, ABC):
    _current_mileage
    _last_service_mileage

    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self._current_mileage = current_mileage
        self._last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000

    @abstractmethod
    def needs_service(self):
        pass
