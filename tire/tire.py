from abc import ABC

class Tire(ABC):
    @abstractmethod
    def need_service(self):
        pass