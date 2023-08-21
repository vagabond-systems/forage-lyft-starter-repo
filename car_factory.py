from car_module import Serviceable, Car
from car_module.car_components.battery import Battery, NubbinBattery, SpindlerBattery
from car_module.car_components.engine import Engine, CapuletEngine, SternmanEngine, WilloughbyEngine
from datetime import date


#Class to create a car of differnt models
class CarFactory:
    #method to creta a calliope car model
    def create_calliope(current_date:date, last_service_date: date, current_mileage:int, last_service_mileage:int) -> Car:
        calliope_engine = CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        calliope_battery = SpindlerBattery(current_date=current_date,last_service_date=last_service_date)
        return Car(engine=calliope_engine,battery=calliope_battery)

    #method to creta a glissade car model
    def create_glissade(current_date:date, last_service_date: date, current_mileage:int, last_service_mileage:int) -> Car:
        glissade_engine = WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        glissade_battery = SpindlerBattery(current_date=current_date,last_service_date=last_service_date)
        return Car(engine=glissade_engine,battery=glissade_battery)
    
    #method to creta a palindrome car model
    def create_palindrome(current_date:date, last_service_date: date, warning_light_on:bool) -> Car :
        palindrome_engine = SternmanEngine(warning_light_is_on=warning_light_on)
        palindrome_battery = SpindlerBattery(current_date=current_date,last_service_date=last_service_date)
        return Car(engine=palindrome_engine,battery=palindrome_battery)

    #method to creta a rorschach car model
    def create_rorschach(current_date:date, last_service_date: date, current_mileage:int, last_service_mileage:int) -> Car :
        rorschach_engine = WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        rorschach_battery = NubbinBattery(current_date=current_date,last_service_date=last_service_date)
        return Car(engine=rorschach_engine,battery=rorschach_battery)

    #method to creta a thovex car model
    def create_thovex(current_date:date, last_service_date: date, current_mileage:int, last_service_mileage:int) -> Car :
        thovex_engine = CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        thovex_battery = NubbinBattery(current_date=current_date,last_service_date=last_service_date)
        return Car(engine=thovex_engine,battery=thovex_battery)
    