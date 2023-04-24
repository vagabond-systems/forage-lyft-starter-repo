from abc import ABC
from typing import List
from tires.tires import Tires

class CarriganTires(Tires, ABC):
    def __init__(self, tire_wear):
        super().__init__()
        self.tire_wear = tire_wear
        
    def needs_service(self, tire_wear: list[float]) -> bool:
        for wear in tire_wear:
            if wear >= 0.9:
                return True
        return False


# class CarriganTires(Tires, ABC):
#     def __init__(self, tire_wear: list[float]):
#         super().__init__(tire_wear)
#         self.tire_wear = tire_wear

#     def needs_service(self, tire_wear: list[float]) -> bool:
#         for wear in tire_wear:
#             if wear >= 0.9:
#                 return True
#         return False