from abc import abstractmethod
from serviceable import Serviceable

class Engine(Serviceable):
    @property
    def current_mileage(self) -> int:
        pass

    @property
    def last_service_mileage(self) -> int:
        pass

#########################################################################

class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self._current_mileage = current_mileage
        self._last_service_mileage = last_service_mileage

    @property
    def current_mileage(self) -> int:
        return self._current_mileage

    @current_mileage.setter
    def current_mileage(self, value):
        self._current_mileage = value

    @property
    def last_service_mileage(self) -> int:
        return self._last_service_mileage

    @last_service_mileage.setter
    def last_service_mileage(self, value) -> None:
        self._last_service_mileage = last_service_mileage

    ## Should be serviced once every 30000 miles
    def needs_service(self) -> bool:
        return self._current_mileage - self._last_service_mileage >= 30000

#########################################################################

class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on = False):
        self._warning_light_is_on = warning_light_is_on

    @property
    def warning_light_is_on(self) -> bool:
        return self._warning_light_is_on

    @warning_light_is_on.setter
    def warning_light_is_on(self, value):
        if(value == "RESET"):
            self._warning_light_is_on = False

    ## Should be serviced only when the warning indicator is on
    def needs_service(self) -> bool:
        return self._warning_light_is_on

#########################################################################

class WilloughbyEngine():
    def __init__(self, current_mileage, last_service_mileage):
        self._current_mileage = current_mileage
        self._last_service_mileage = last_service_mileage

    @property
    def current_mileage(self) -> int:
        return self._current_mileage

    @current_mileage.setter
    def current_mileage(self, value):
        self._current_mileage = value

    @property
    def last_service_mileage(self) -> int:
        return self._last_service_mileage

    @last_service_mileage.setter
    def last_service_mileage(self, value) -> None:
        self._last_service_mileage = last_service_mileage

    ## Should be serviced once every 60000 miles
    def needs_service(self) -> bool:
        return self._current_mileage - self._last_service_mileage >= 60000
