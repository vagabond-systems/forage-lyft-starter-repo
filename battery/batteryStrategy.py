from abc import ABC, abstractmethod


class IBatteryStrategy(ABC):
    @abstractmethod
    def needs_service():
        pass
