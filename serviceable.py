from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        """
        Checks if the object needs service.

        This method should be implemented by classes that are serviceable.
        It should perform checks to determine if the object requires any maintenance or service.
        The specific implementation will vary based on the type of serviceable object.

        Returns:
            bool: True if the object needs service, False otherwise.
        """
        pass
