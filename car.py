from Serviceable import Serviceable
from Battery import Battery
class Car(Serviceable, Battery):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass
