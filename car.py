from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date,last_service_mileage,current_date):
        self.last_service_date = last_service_date
        self.last_service_mileage = last_service_mileage
        self.current_date = current_date

    @abstractmethod
    def needs_service(self):
        pass

