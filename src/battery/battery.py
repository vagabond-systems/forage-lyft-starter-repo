from abc import ABC, abstractmethod


class Battery(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def battery_should_be_serviced(self):
        pass
