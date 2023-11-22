from serviceable import Serviceable
from tire.CarriganTires import CarriganTires
from tire.OctoprimeTires import OctoprimeTires



class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()

    def check_tire_service(self):
        """Tire service"""
        if isinstance(self.tires, CarriganTires):
            return any(tire_wear >= 0.9 for tire_wear in self.tires.wear_array)
        elif isinstance(self.tires, OctoprimeTires):
            return sum(self.tires.wear_array) >= 3
        else:
            return False
