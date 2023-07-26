from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def need_service(self) -> bool:
        pass