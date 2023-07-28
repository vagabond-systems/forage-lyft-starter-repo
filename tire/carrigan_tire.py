from abc import ABC
from car import Serviceable

class CarriganTire(Serviceable, ABC):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        return max(self.tire_wear) >= 0.9
