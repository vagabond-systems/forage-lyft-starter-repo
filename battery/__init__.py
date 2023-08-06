from abc import ABC, abstractmethod
class Battery:
    @abstractmethod
    def needs_service(self) -> bool:
        pass