from abc import ABC, abstractmethod

class Servisable(ABC):
    @abstractmethod
    def needs_service():
        pass