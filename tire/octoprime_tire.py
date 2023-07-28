from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def need_service(self):
        return sum(self.tire_wear_array) >= 3