from servicable import IServiceable


class Car(IServiceable):
    def __init__(self, engineStrategy, batterySrategy, tireStrategy):
        self.engineStrategy = engineStrategy
        self.batteryStrategy = batterySrategy
        self.tireStrategy = tireStrategy

    def needs_service(self):
        if self.engineStrategy.needs_service() or self.batteryStrategy.needs_service() or self.tireStrategy.needs_service():
            return True
        else:
            return False
