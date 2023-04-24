from abc import ABC

from tires.tires import Tires

class OctoprimeTires(Tires, ABC):
        def __init__(self, tire_wear):
            super().__init__()
            self.tire_wear = tire_wear

        def needs_service(self, tire_wear: list[float]) -> bool:
            wear = sum(tire_wear)
            if wear >= 3:
                return True
            return False


    # def needs_service(self, tire_wear: list[float]) -> bool:
    #     total_wear = sum(tire_wear)
    #     if total_wear >= 3:
    #         return True
    #     return False
