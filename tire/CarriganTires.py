
from serviceable import Serviceable


class CarriganTires:
    def __init__(self, wear_array):
        self.wear_array = wear_array

    def needs_service(self):
        """Check if Carrigan tires need service"""
        return any(tire_wear >= 0.9 for tire_wear in self.wear_array)

