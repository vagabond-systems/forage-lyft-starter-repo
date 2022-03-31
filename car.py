from abc import ABC, abstractmethod
from servicable import Servicable

class Car(Servicable,ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

