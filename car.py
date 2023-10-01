from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
        

    def needs_service(self):
        return self.engine.service_needed() or self.battery.service_needed()
