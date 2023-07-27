from car import Car
from datetime import date
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery import NubbinBattery
from battery import SplinderBattery


class Carfactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage, last_service_mileage) -> Car:
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SplinderBattery(current_date,last_service_date)
        return Car(engine, battery)
    
    def create_glissade(self, current_date: date, last_service_date: date, current_mileage, last_service_mileage) -> Car:
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SplinderBattery(current_date,last_service_date) 
        return Car(engine, battery)
    
    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SplinderBattery(current_date,last_service_date)
        return Car(engine, battery)
    
    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage, last_service_mileage) -> Car:
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        return Car(engine, battery)
    
    def create_thovex(self, current_date: date, last_service_date: date, current_mileage, last_service_mileage) -> Car:
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        return Car(engine, battery)