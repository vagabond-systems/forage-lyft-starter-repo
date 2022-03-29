from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def needs_service(self) -> bool:
        return super().needs_service()