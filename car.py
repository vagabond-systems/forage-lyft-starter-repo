from abc import ABC, abstractmethod
from datetime import datetime

class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        current_date = datetime.now()
        # Check if the car needs service based on some logic
        # For example, we'll assume it needs service if more than 365 days have passed since the last service
        days_since_last_service = (current_date - self.last_service_date).days
        return days_since_last_service > 365

