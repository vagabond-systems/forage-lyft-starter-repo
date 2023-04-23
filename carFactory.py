from car import Car
from battery.created_batteries import nubbin_battery, spindler_battery
from engine.created_engines import capulet_engine, sternman_engine, willoughby_engine

class CarFactory():
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(current_date, last_service_date)

        car = Car(engine, battery)
        return car
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine=willoughby_engine.WilloughbyEngine(current_mileage,last_service_mileage)
        battery=spindler_battery.SpindlerBattery(current_date,last_service_date)

        car = Car(engine, battery)
        return car
    
    def create_palindrome(self, current_date, last_service_date, warning_light_is_on):
        engine=sternman_engine.SternmanEngine(warning_light_is_on)
        battery=spindler_battery.SpindlerBattery(current_date,last_service_date)
        
        car = Car(engine, battery)
        return car
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine=willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        battery=nubbin_battery.NubbinBattery(current_date,last_service_date)

        car = Car(engine, battery)
        return car
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery=nubbin_battery.NubbinBattery(current_date,last_service_date)

        car = Car(engine, battery)
        return car
