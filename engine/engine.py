from abc import ABC

from car import Car

from datetime import datetime



class Engine(Car, ABC):
    def __init__(self, last_service_date=datetime.now, warning_light_is_on=None):
        pass

    def needs_service(self):
        pass