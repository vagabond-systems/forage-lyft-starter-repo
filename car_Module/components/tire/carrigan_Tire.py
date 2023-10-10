from car_Module.components.tire.tire_Interface import Tire
from typing import List

class CarriganTire(Tire):
    def __init__(self, tire_wear :List[float]):
        self.tire_wear = tire_wear

    def needs_service(self) ->bool:
        for value in self.tire_wear :
            if value >= 0.9:
                return True
        return False