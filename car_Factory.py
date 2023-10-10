#importing necessary libraries
from car_Module import Serviceable, Car
from car_Module.components.battery import Battery, NubbinBattery, SpindlerBattery
from car_Module.components.engine import Engine, CapuletEngine, SternmanEngine, WilloughbyEngine
from car_Module.components.tire import Tire, CarriganTire, OctoprimeTire
from typing import List
from datetime import date


#CarFactory class to create all available models 
class CarFactory:
    #create_calliope method
    #calliope uses Capulet engine
    #calliope uses Spindler battery
    def create_calliope(current_date:date, last_service_date: date, current_mileage:int, last_service_mileage:int, tire_wear:List[float]) -> Car:
        calliope_engine = CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        calliope_battery = SpindlerBattery(current_date=current_date,last_service_date=last_service_date)
        tire = CarriganTire(tire_wear=tire_wear)
        return Car(engine=calliope_engine,battery=calliope_battery,tire=tire)

    #create_glissade method
    #calliope uses Willoughby engine
    #calliope uses Spindler battery
    def create_glissade(current_date:date, last_service_date: date, current_mileage:int, last_service_mileage:int, tire_wear:List[float]) -> Car:
        glissade_engine = WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        glissade_battery = SpindlerBattery(current_date=current_date,last_service_date=last_service_date)
        tire = CarriganTire(tire_wear=tire_wear)
        return Car(engine=glissade_engine,battery=glissade_battery,tire=tire)
    
    #create_palindrome method
    #calliope uses Sternman Engine
    #calliope uses Spindler battery
    def create_palindrome(current_date:date, last_service_date: date, warning_light_on:bool, tire_wear:List[float]) -> Car :
        palindrome_engine = SternmanEngine(warning_light_is_on=warning_light_on)
        palindrome_battery = SpindlerBattery(current_date=current_date,last_service_date=last_service_date)
        tire = OctoprimeTire(tire_wear=tire_wear)
        return Car(engine=palindrome_engine,battery=palindrome_battery,tire=tire)

    #create_rorschach method
    #calliope uses Willoughby engine
    #calliope uses Nubbin battery
    def create_rorschach(current_date:date, last_service_date: date, current_mileage:int, last_service_mileage:int, tire_wear:List[float]) -> Car :
        rorschach_engine = WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        rorschach_battery = NubbinBattery(current_date=current_date,last_service_date=last_service_date)
        tire = CarriganTire(tire_wear=tire_wear)
        return Car(engine=rorschach_engine,battery=rorschach_battery,tire=tire)

    #create_thovex method
    #calliope uses Capulet engine
    #calliope uses Nubbin battery
    def create_thovex(current_date:date, last_service_date: date, current_mileage:int, last_service_mileage:int, tire_wear:List[float]) -> Car :
        thovex_engine = CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        thovex_battery = NubbinBattery(current_date=current_date,last_service_date=last_service_date)
        tire = OctoprimeTire(tire_wear=tire_wear)
        return Car(engine=thovex_engine,battery=thovex_battery)
    