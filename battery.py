from abc import ABC, abstractmethod
from datetime import datetime


class Battery(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
      pass