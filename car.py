from abc import ABC, abstractmethod
from servicable import Servicable


class Car(Servicable):
    def __init__(self, battery, engine):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
