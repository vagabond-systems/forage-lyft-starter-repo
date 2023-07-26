from abc import ABC
from car import Serviceable
from datetime import datetime, timedelta

class NubbinBattery(Serviceable, ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        return (datetime.today().date() - self.last_service_date) > timedelta(days=365*5)
