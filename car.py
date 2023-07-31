from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, last_service_date, engine, battery):
        self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        # Check if either the engine or the battery needs service
        return self.engine.needs_service() or self.battery.needs_service()
