from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def engine_should_be_serviced(self):
        pass
