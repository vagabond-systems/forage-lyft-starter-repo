from car import Car
from battery.nubbinbattery import NubbinBattery
from battery.spindlerbattery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tirewearreading):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tirewearreading) 
        car = Car(engine, battery, tires)
        return car

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tirewearreading):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tirewearreading) 
        car = Car(engine, battery, tires)
        return car

    def create_palindrome(current_date, last_service_date, warning_light_is_on, tirewearreading):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoprimeTires(tirewearreading)
        car = Car(engine, battery, tires)
        return car

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tirewearreading):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(tirewearreading)
        car = Car(engine, battery, tires)
        return car

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tirewearreading):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTires(tirewearreading) 
        car = Car(engine, battery, tires)
        return car




    
