from abc import ABC, abstractmethod
from serviceable import Serviceable

class Battery(Serviceable):
    @abstractmethod
    def need_service(self) -> bool:
        pass