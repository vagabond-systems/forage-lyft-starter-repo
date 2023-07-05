from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, last_service_date):
        """
        Initialize the Car object with the last service date.

        Parameters:
        last_service_date (datetime.date): The date when the car was last serviced.
        """
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        """
        Abstract method to check if the car needs service.

        This method must be implemented in the subclasses.

        Returns:
        bool: True if the car needs service, False otherwise.
        """
        pass
