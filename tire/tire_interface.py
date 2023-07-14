from abc import abstractmethod
from sensor.tire_sensor import TireSensor

class TireInterface(TireSensor):
    
    def __init__(self, sensors):
        super().__init__(sensors)

    @abstractmethod
    def needs_service():
        pass    