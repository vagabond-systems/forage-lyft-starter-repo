from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def serviceNeed(self):
        pass