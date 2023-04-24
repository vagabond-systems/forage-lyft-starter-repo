from abc import ABC, abstractmethod

class Tires(ABC):
    @abstractmethod
    def needs_service(self, tire_type, tire_wear: list[float]) -> bool:
        pass
