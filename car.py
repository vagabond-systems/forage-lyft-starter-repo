from abc import ABC, abstractmethod
from datetime import datetime


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass

    def needs_tire_service(self, tire_wear_array, tire_value):
        for value in tire_wear_array:
            if value >= tire_value:
                return True
        return False


class Battery:
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 3
        )

    def needs_service(self):
        if self.service_threshold_date < datetime.today().date():
            return True
        else:
            return False
