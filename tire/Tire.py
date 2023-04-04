from abc import ABC, abstractmethod

class Tire(ABC):

    @abstractmethod
    def needs_service(self):
        pass