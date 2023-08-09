from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
