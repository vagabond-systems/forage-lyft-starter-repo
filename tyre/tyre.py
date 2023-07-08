from abc import ABC, abstractmethod

class Tyre(ABC):
    @abstractmethod
    def tyres_needs_service(self):
        pass