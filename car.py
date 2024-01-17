#  i notice that we haven't imported engine or battery here
from service import Service
from abc import ABC

class Car(ABC):
    def __init__(self, last_service_date):
        self.engine = engine
        self.battery = battery

#  we have the liberty to decide the operation of needs_service, so long as it returns a boolean
        # this is probably because we used strategy method
    def needs_service(self) -> bool:
        # if the result of the needs_service function in either engine or battery class is true, we return a true
        return self.engine.needs_service() or self.battery.needs_service()

