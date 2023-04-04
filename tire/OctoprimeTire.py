from tire.Tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tires_array):
        self.tires_array = tires_array

    def needs_service(self):
        return sum(self.tires_array) >= 3