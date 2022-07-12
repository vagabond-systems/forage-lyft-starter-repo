from abc import ABC, abstractmethod

class Servicable(ABC):
    @abstractmethod
    def needs_service(self):
        pass