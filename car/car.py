from car.serviceable import Serviceable


# car class that has an engine and battery
class Car(Serviceable):
    def __init__(self, engine, battery):
        self.battery = battery
        self.engine = engine

    # method calls engine's service method and battery's service method to make a decision for service
    def needs_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced()
