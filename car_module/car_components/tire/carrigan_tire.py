from car_module.car_components.tire.tire_interface import Tire
from typing import List

class CarriganTire(Tire):
    def __init__(self, tire_wear :List[float]):
        self.tire_wear = tire_wear

    def needs_service(self) ->bool:
        for value in self.tire_wear :
            if self.tire_wear >= 0.9:
                return True
        return False