from car_module import Car
from car_module.components.battery import NubbinBattery, SpliderBattery
from car_module.components.engine import CapuletEngine, SternmanEngine, WillounghbyEngine
from datetime import date

class CarFactory : 
    def create_calliope(current_date : date, last_sevice_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        calliope_engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        calliope_battery = SpliderBattery(current_date=current_date, last_service_date=last_sevice_date)
        return Car(engine=calliope_engine, battery=calliope_battery)


    def create_glissade (current_date : date, last_service_date : date, current_mileage: int, last_service_mileage : int) -> Car :
        glissad_engine = WillounghbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        glissad_battery = SpliderBattery(current_date=current_date, last_service_date=last_service_date)
        return Car(engine=glissad_engine, battery=glissad_battery)

    def create_palindrome (current_date : date, last_service_date : date, warning_light_on : bool) -> Car:
        palindrome_engine = SternmanEngine(warning_light_is_on=warning_light_on)
        palindrome_battery = SpliderBattery(current_date=current_date, last_service_date=last_service_date)
        return Car(engine=palindrome_engine, battery=palindrome_battery)
    
    def create_rorschach (current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        rorschach_engine = WillounghbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        rorschach_battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        return Car(engine=rorschach_engine, battery=rorschach_battery)
    
    def create_thovex (current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car :
        thovex_engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        thovex_battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)

        return Car(engine=thovex_engine, battery=thovex_battery)