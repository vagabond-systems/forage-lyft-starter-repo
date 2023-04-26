from abc import ABC, abstractmethod


class IServiceable(ABC):
    @abstractmethod
    def needs_service():
        pass
