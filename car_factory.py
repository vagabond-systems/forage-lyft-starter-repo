from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.splinder_battery import SplinderBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class Carfactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SplinderBattery(current_date,last_service_date)
        tires = CarriganTires(tire_wear)
        return Car(engine, battery, tires)
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SplinderBattery(current_date,last_service_date) 
        tires = OctoprimeTires(tire_wear)
        return Car(engine, battery, tires)
    
    def create_palindrome(self, current_date, last_service_date, warning_light_on, tire_wear) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SplinderBattery(current_date,last_service_date)
        tires = CarriganTires(tire_wear)
        return Car(engine, battery, tires)
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        tires = OctoprimeTires(tire_wear)
        return Car(engine, battery, tires)
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        tires = CarriganTires(tire_wear)
        return Car(engine, battery, tires)