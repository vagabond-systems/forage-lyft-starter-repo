from tires.tire import Tire
from collections import Counter


class CarriganTires(Tire):
    def __init__(self, tires_condition: []) -> None:
        self.__tires_condition = tires_condition

    def needs_service(self):
        check = 0
        for val in self.__tires_condition:
            if val >= 0.9:
                return True
        return False
