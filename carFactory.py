from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from tire.carrigan_tires import CarriganTires
from tire.octoprime_tires import OctoprimeTires

from car import Car

class carFactory(Car):
    
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, sensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTires(sensors)
        car = Car(engine, battery, tire)
        return car
        
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, sensors):  
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = OctoprimeTires(sensors)
        car = Car(engine, battery, tire)
        return car

        
    def create_palindrome(self,current_date, last_service_date, warning_light_on, sensors):
        engine = SternmanEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTires(sensors)
        car = Car(engine, battery, tire)
        return car

        
    def create_rorschach(self,current_date, last_service_date, current_mileage, last_service_mileage, sensors):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = OctoprimeTires(sensors)
        car = Car(engine, battery, tire)
        return car

        
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, sensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = CarriganTires(sensors)
        car = Car(engine, battery, tire)
        return car
  
        
        