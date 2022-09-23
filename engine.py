from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

#########################################################################

class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    ## Should be serviced once every 30000 miles
    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 30000

#########################################################################

class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    ## Should be serviced only when the warning indicator is on
    def needs_service(self) -> bool:
        return self.warning_light_is_on

#########################################################################

class WilloughbyEngine():
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    ## Should be serviced once every 60000 miles
    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 60000
