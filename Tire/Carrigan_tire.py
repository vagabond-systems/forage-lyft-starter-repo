from Tire.Tire import Tire
from car import Car

class Carrigan_tire(Tire, Car):
    def needs_service(self):
        for value in self.value_of_worn_in_tire:
           if value>=0.9:
              return True
        return False
