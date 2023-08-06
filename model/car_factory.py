from datetime import date
from car import Car
from engine.capulet_engine import CapuletEngine 
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, sensor_response_array: list) -> Car: 
        return Car(CapuletEngine(current_mileage,last_service_mileage), SpindlerBattery(current_date, last_service_date), CarriganTire(sensor_response_array))
    
    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, sensor_response_array: list) -> Car: 
        return Car(WilloughbyEngine(current_mileage,last_service_mileage), SpindlerBattery(current_date, last_service_date), CarriganTire(sensor_response_array))
    
    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, sensor_response_array: list) -> Car: 
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(current_date, last_service_date), CarriganTire(sensor_response_array))
    
    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, sensor_response_array: list) -> Car: 
        return Car(WilloughbyEngine(current_mileage,last_service_mileage), NubbinBattery(current_date, last_service_date), OctoprimeTire(sensor_response_array))
    
    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, sensor_response_array: list) -> Car:
        return Car(CapuletEngine(current_mileage,last_service_mileage), SpindlerBattery(current_date, last_service_date), CarriganTire(sensor_response_array))