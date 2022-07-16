from abc import ABC
from car import Car
from capulet_engine import CapuletEngine
from Battery.SplinderBattery import SplinderBattery
from willoughby_engine import WilloughbyEngine
from Battery.NubbinBattery import NubbinBattery
from sternman_engine import SternmanEngine


class CarFactory(Car, ABC): 
    def __init__(self) -> None:
        pass
    
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        self.engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.battery = SplinderBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(self.engine, self.battery)
        
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        self.engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(self.engine, self.battery)
    
    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        self.engine = SternmanEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(self.engine, self.battery)
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        self.engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.battery = SplinderBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(self.engine, self.battery)
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        self.engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(self.engine, self.battery)
    
    
    def need_service(self):
        return super().need_service()
