from abc import ABC, abstractmethod

#  this is an abstract class, therefore, it would have the decorator of abstractmethod
class Service(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass