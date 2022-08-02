from abc import ABC, abstractmethod

from serviceable import Serviceable

class Car(Serviceable, ABC):
    _engine
    _battery

    def __init__(self, last_service_date, engine, battery):
        self.last_service_date = last_service_date
        self._engine = engine
        self._battery = battery

    @abstractmethod
    def needs_service(self):
        pass