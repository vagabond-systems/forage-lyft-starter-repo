from abc import abstractmethod
from service import Servicable


class Car(Servicable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        self.engine.need_services() or self.battery.needs_service()
