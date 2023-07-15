from abc import ABCMeta, abstractmethod


class IBattery(metaclass=ABCMeta):

    def __init__(self, last_service_date, current_date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def get_current_date(self):
        return self.current_date

    def get_last_service_date(self):
        return self.last_service_date

    @abstractmethod
    def needs_service():
        pass
