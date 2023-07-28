from abc import ABC
from car import Serviceable

class OctoprimeTire(Serviceable, ABC):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        return sum(self.tire_wear) >= 3
