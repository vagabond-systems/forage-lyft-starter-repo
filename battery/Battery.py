from abc import ABC, abstractmethod


class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass