from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def engine_should_be_serviced(self) -> bool:
        """
        method to check if engine needs to be serviced on an instance
        """
        pass
