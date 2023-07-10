from abc import ABC


class Battery(ABC):
    def needs_service(self):
        """
        Checks if the battery needs servicing.

        This method should be implemented by concrete battery classes.
        It should perform checks to determine if the battery requires any maintenance or service.
        The specific implementation will depend on the type of battery being used.

        Returns:
            bool: True if the battery needs service, False otherwise.
        """
        pass