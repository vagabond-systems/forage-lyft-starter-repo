from abc import ABC, abstractmethod
from datetime import datetime ,date
# from engine.Battery.spindler import SpindlerBattery
# from engine.Battery.Nubbin import NubbinBattery
# from engine.capulet_engine import CapuletEngine

class Car(ABC):
    def __init__(self):
        # self.engine =  engine
        # self.battery = battery
        pass

    @abstractmethod
    def needs_service(self):
        pass


class Engine(Car):
    def __init__(self) -> None:
        # self.current_mileage= engineClass.current_mileage
        # self.last_service_mileage = engineClass.last_service_mileage
        # self.mil = engineClass.mil
        pass
        # self.engineClass =engineClass
        
    def needs_service(self):
        return self.engineClass.engine_should_be_serviced()

class Battery(Car):
    def __init__(self) -> None:
        # self.last_service_date= batteryClass.last_service_date
        # self.threshold_year = batteryClass.threshold_year
        # self.current_date = datetime.today().date()
        pass
        # self.batteryClass = batteryClass
    
    def needs_service(self):
        return self.batteryClass.engine_should_be_serviced()


