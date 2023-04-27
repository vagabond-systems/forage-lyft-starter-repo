from servicable import IServiceable
from engine.engineStrategy import IEngineStrategy
from battery.batteryStrategy import IBatteryStrategy


class Car(IServiceable):
    def __init__(self, engineStrategy, batterySrategy):
        self.engineStrategy = engineStrategy
        self.batteryStrategy = batterySrategy

    def needs_service(self):
        if self.engineStrategy.needs_service() or self.batteryStrategy.needs_service():
            return True
        else:
            return False
