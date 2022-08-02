from abc import ABC

from engine import Engine

class CapuletEngine(Engine, ABC):
    _current_mileage
    _last_service_mileage

    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self._current_mileage = current_mileage
        self._last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self._current_mileage - self._last_service_mileage > 30000
    
    @abstractmethod
    def needs_service(self):
        pass
        
