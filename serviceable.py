from abc import ABC, abstractmethod

# Serviceable Interface
class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass
