from Serviceable.Car import Car
from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery
from engine.CapuletEngine import CapuletEngine
from engine.SternmanEngine import SternmanEngine
from engine.WilloughbyEngine import WilloughbyEngine
from tire.CarriganTires import CarriganTires
from tire.OctoprimeTires import OctoprimeTires


class CarFactory:

    @staticmethod
    def create_callopie(current_date, last_service_date, current_mileage, last_service_mileage, tires_array):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tires_array) 

        return Car(engine, battery, tires)
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage,tires_array):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTires(tires_array) 

        return Car(engine, battery, tires)
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tires_array):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tires_array) 


        return  Car(engine, battery, tires)
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage,tires_array):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTires(tires_array) 

        return Car(engine, battery,tires)
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage,tires_array):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(tires_array) 

        return Car(engine, battery, tires)