from car_module.car_components.tire.tire_interface import Tire
from typing import List

class OctoprimeTire(Tire):
    def __init__(self, tire_wear :List[float]):
        self.tire_wear = tire_wear

    def needs_service(self) ->bool:
        return sum(self.tire_wear) >= 3