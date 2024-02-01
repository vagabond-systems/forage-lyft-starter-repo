from abc import ABC

from car import Car

from datetime import datetime



class BatteryInterface(Car, ABC):
    def __init__(self, last_service_date=datetime.today().date()):
        pass

    def needs_service(self):
        pass