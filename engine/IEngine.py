from abc import ABCMeta, abstractmethod


class IEngine(metaclass=ABCMeta):

    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
