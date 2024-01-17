from abc import ABC, abstractmethod
import engine, battery.battery as battery


class Car(ABC):
    def __init__(self, last_service_date):
        self.engine: Engine()
        self.battery: Battery()

    @abstractmethod
    def needs_service(self) -> bool:
        pass
