from abc import ABC, abstractmethod

class IEngineStrategy(ABC):
    @abstractmethod
    def needs_service():
        pass