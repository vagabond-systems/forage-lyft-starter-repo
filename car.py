from abc import ABC, abstractmethod
from engine.engine import Engine
from battery.battery import Battery


class Car():

    def __init__(self, last_service_date, Engine, Battery):
        self.last_service_date = last_service_date
        self.engine = Engine()
        self.battery = Battery()

    @abstractmethod
    def needs_service(self):
        pass
