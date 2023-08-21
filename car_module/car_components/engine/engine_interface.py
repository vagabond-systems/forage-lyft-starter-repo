from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def needs_service() -> bool:
        pass
