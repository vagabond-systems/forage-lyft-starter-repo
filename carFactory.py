from abc import ABC, abstractmethod
from serviceable import Serviceable
from datetime import datetime
from car import Car
import engines
import batteries

class CarFactory:

    @staticmethod
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        engine = engines.CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        battery = batteries.SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(engine=engine, battery=battery)

    @staticmethod
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        engine = engines.WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        battery = batteries.SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(engine=engine, battery=battery)    

    @staticmethod
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool):
        engine = engines.SternmanEngine(warning_light_on=warning_light_on)
        battery = batteries.SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(engine=engine, battery=battery)
    
    @staticmethod
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        engine = engines.WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        battery = batteries.NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(engine=engine, battery=battery)
    
    @staticmethod
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        engine = engines.CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        battery = batteries.NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(engine=engine, battery=battery)