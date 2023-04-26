from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self, last_service_date):
        super().__init__()
        self.last_service_date = last_service_date
    
    @abstractmethod
    def needs_service(self):
        pass
