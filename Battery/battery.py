from abc import ABC, abstractmethod

from Serviceable import Serviceable

class Battery(Serviceable, ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def need_service(self):
        pass