#import necessary libraries
from abc import ABC, abstractmethod

#Serviceable abstraction method
class Serviceable(ABC):
    @abstractmethod
    def needs_service() -> bool:
        pass