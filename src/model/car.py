from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return (
            self.engine.engine_should_be_serviced()
            and self.battery.battery_should_be_serviced()
        )
