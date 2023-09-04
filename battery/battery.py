from abc import ABC, abstractmethod



class Battery(ABC):
    def needs_service(self):
        pass