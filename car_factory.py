from battery.NubbinBattery import NubbinBattery
from battery.SplinderBattery import SplinderBattery
from car import Car
from datetime import date
from engine.CapuletEngine import CapuletEngine
from engine.SternmanEngine import SternmanEngine
from engine.WilloughbyEngine import WilloughbyEngine
from tires.CarriganTires import CarriganTires
from tires.OctoPrimeTires import OctoPrimeTires

class CarFactory:
    def create_calliope(self,current_mileage:int,last_service_mileage:int,current_date:date,last_service_date:date,tire_wear) -> Car:
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SplinderBattery(current_date,last_service_date)
        tires = OctoPrimeTires(tire_wear)
        return Car(engine,battery,tires)
    
    def create_glissade(self,current_mileage:int,last_service_mileage:int,current_date:date,last_service_date:date,tire_wear) -> Car:
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SplinderBattery(current_date,last_service_date)
        tires = CarriganTires(tire_wear)
        return Car(engine,battery,tires)
    
    def create_palindrome(self,warning_light_on:bool,current_date:date,last_service_date:date,tire_wear) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SplinderBattery(current_date,last_service_date)
        tires = OctoPrimeTires(tire_wear)
        return Car(engine,battery,tires)
    
    def create_rorschach(self,current_mileage:int,last_service_mileage:int,current_date:date,last_service_date:date,tire_wear) -> Car:
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        tires = CarriganTires(tire_wear)
        return Car(engine,battery,tires)
    
    def create_thovex(self,current_mileage:int,last_service_mileage:int,current_date:date,last_service_date:date,tire_wear) -> Car:
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        tires = OctoPrimeTires(tire_wear)
        return Car(engine,battery,tires)