from Tire.Tire import Tire
from car import Car

class OctoprimeTire(Tire, Car):
    def needs_service(self):
        for value in self.value_of_worn_in_tire:
            sum+= value
        if sum >= 3:
            return True
        else:
            return False
