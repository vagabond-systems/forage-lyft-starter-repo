from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date, value_of_worn_in_tire):
        self.last_service_date = last_service_date
        self.value_of_worn_in_tire= value_of_worn_in_tire

    @abstractmethod
    def needs_service(self):
        pass
