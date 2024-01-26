from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery,tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced() or self.tire.tire_should_be_serviced()