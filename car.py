from abc import ABC, abstractmethod
from datetime import datetime


class Car(ABC):
    def __init__(self, engine, battery):
        engine(last_service_date=engine.last_service_date, warning_light_is_on = engine.warning_light_is_on)
        battery = battery(last_service_date=datetime.today().date())

    @abstractmethod
    def needs_service(self):
        pass
