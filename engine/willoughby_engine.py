from abc import ABC

from car import Car


class WilloughbyEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        """
        Initialize the WilloughbyEngine object with the last service date, current mileage, and last service mileage.

        Parameters:
        last_service_date (datetime.date): The date when the engine was last serviced.
        current_mileage (int): The current mileage of the engine.
        last_service_mileage (int): The mileage at the time of the last service.
        """
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        """
        Check if the engine should be serviced based on the mileage.

        Returns:
        bool: True if the engine should be serviced, False otherwise.
        """
        return self.current_mileage - self.last_service_mileage > 60000
