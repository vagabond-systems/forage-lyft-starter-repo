from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery

class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass
