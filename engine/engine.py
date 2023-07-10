from abc import ABC


class Engine(ABC):
    def needs_service(self):
        """
        Checks if the engine needs servicing.

        This method should be implemented by concrete engine classes.
        It should perform checks to determine if the engine requires any maintenance or service.
        The specific implementation will depend on the type of engine being used.

        Returns:
            bool: True if the engine needs service, False otherwise.
        """
        pass
    