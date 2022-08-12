from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def needs_service():
        pass
