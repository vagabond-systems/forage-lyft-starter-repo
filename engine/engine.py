from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        """
        method to check if engine needs to be serviced on an instance
        """
        pass
