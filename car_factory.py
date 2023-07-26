from battery.NubbinBattery import NubbinBattery
from battery.SplinderBattery import SplinderBattery
from car import Car
from datetime import date
from engine.CapuletEngine import CapuletEngine
from engine.SternmanEngine import SternmanEngine
from engine.WilloughbyEngine import WilloughbyEngine

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