from tires.tire import Tire


class OctoprimeTires(Tire):
    def __init__(self, tires_condition: []) -> None:
        self.__tires_condition = tires_condition

    def needs_service(self):
        return sum(self.__tires_condition) >= 3
