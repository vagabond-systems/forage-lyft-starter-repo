from abc import ABC , abstractmethod
from datetime import date

class Serviceable(ABC):
    @abstractmethod
    def need_service(self) -> bool:
        pass

class Engine(Serviceable):
    @abstractmethod
    def need_service(self) -> bool:
        pass

class Battery(Serviceable):
    @abstractmethod
    def need_service(self) -> bool:
        pass
    
class CapuletEngine(Engine):
    def __init__(self,last_service_mileage:int,current_mileage:int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    
    def need_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 30000

class WilloughbyEngine(Engine):
    def __init__(self,last_service_mileage:int,current_mileage:int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def need_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 60000

class SternmanEngine(Engine):
    def __init__(self,warning_light_on:bool):
        self.warning_light_on = warning_light_on

    def need_service(self) -> bool:
        return self.warning_light_on

class SplinderBattery(Battery):
    def __init__(self,last_service_date:date,current_date:date):  
        self.last_service_date = last_service_date
        self.current_date = current_date

    def need_service(self) -> bool:
        return self.current_date - self.last_service_date >= 730

class NubbinBattery(Battery):
    def __init__(self,last_service_date:date,current_date:date):  
        self.last_service_date = last_service_date
        self.current_date = current_date 
    
    def need_service(self) -> bool:
        return self.current_date - self.last_service_date >= 1460

class Car(Serviceable):
    def __init__(self,engine:Engine,battery:Battery):
        self.engine = engine
        self.battery = battery
        
    def need_service(self) -> bool:
        return self.engine.need_service() or self.battery.need_service()

class CarFactory:
    def create_calliope(self,current_mileage:int,last_service_mileage:int,current_date:date,last_service_date:date) -> Car:
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SplinderBattery(current_date,last_service_date)
        return Car(engine,battery)
    
    def create_glissade(self,current_mileage:int,last_service_mileage:int,current_date:date,last_service_date:date) -> Car:
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SplinderBattery(current_date,last_service_date)
        return Car(engine,battery)
    
    def create_palindrome(self,warning_light_on:bool,current_date:date,last_service_date:date) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SplinderBattery(current_date,last_service_date)
        return Car(engine,battery)
    
    def create_rorschach(self,current_mileage:int,last_service_mileage:int,current_date:date,last_service_date:date) -> Car:
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        return Car(engine,battery)
    
    def create_thovex(self,current_mileage:int,last_service_mileage:int,current_date:date,last_service_date:date) -> Car:
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        return Car(engine,battery)
    