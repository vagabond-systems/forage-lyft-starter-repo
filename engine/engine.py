from abc import ABC

from car import Car

class Engine(Car,ABC):
    def __init__(self,last_service_date):
        super().__init__(last_service_date)
