from tire.Tire import Tire


class CarriganTire(Tire):
    def __init__(self, tires_array):
        self.tires_array = tires_array

    def needs_service(self):
        return max(self.tires_array) >= 0.9

    # def needs_service(self):
    #     self.tires_array = [x for x in self.tires_array if x >= 0.9]
    #     return len(self.tires_array) > 0
    #
    # def needs_service(self):
    #     for i in len(self.tires_array):
    #         if self.tires_array[i] >= 0.9:
    #             return True
    #     return False