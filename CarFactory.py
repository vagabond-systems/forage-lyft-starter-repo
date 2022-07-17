from abc import ABC
from car import Car
from engine.capulet_engine import CapuletEngine
from Battery.SplinderBattery import SplinderBattery
from engine.willoughby_engine import WilloughbyEngine
from Battery.NubbinBattery import NubbinBattery
from engine.sternman_engine import SternmanEngine


class CarFactory(Car, ABC): 
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = SplinderBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(engine, battery)
        
    @staticmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = SplinderBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_is_on) -> Car:
        engine = SternmanEngine(warning_light_is_on=warning_light_is_on)
        battery = SplinderBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(engine, battery)
    
