from abc import ABC

from car import Car


class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        """
        Initialize the SternmanEngine object with the last service date and warning light status.

        Parameters:
        last_service_date (datetime.date): The date when the engine was last serviced.
        warning_light_is_on (bool): The status of the warning light (True if it's on, False otherwise).
        """
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        """
        Check if the engine should be serviced based on the warning light status.

        Returns:
        bool: True if the engine should be serviced, False otherwise.
        """
        return self.warning_light_is_on
