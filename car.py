from servicable import IServiceable
from engine.engineStrategy import IEngineStrategy
from battery.batteryStrategy import IBatteryStrategy


class Car(IServiceable):
    def __init__(self):
        self.engineStrategy = IEngineStrategy
        self.batteryStrategy = IBatteryStrategy

    def needs_service(self):
        pass
