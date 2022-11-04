from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    
    def needs_service(self):
        self.engine.needs_service
        self.battery.needs_service
