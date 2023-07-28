from datetime import datetime
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from battery import SpindlerBattery, NubbinBattery
from tire import CarriganTire, OctoprimeTire
from car import Car

class CarFactory:
    @staticmethod
    def create_calliope(current_mileage, last_service_mileage, last_service_date, tire_type, tire_wear_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)

        if tire_type == "Carrigan":
            tires = CarriganTire(tire_wear_array)
        elif tire_type == "Octoprime":
            tires = OctoprimeTire(tire_wear_array)

        return Car(engine, battery, tires)

    @staticmethod
    def create_glissade(current_mileage,last_service_mileage, last_service_date, tire_type, tire_wear_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)

        if tire_type == "Carrigan":
            tires = CarriganTire(tire_wear_array)
        elif tire_type == "Octoprime":
            tires = OctoprimeTire(tire_wear_array)

        return Car(engine, battery, tires)

    @staticmethod
    def create_palindrome(warning_light_on, tire_type, tire_wear_array):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(datetime.today().date())  # Assume new battery for Palindrome
        
        if tire_type == "Carrigan":
            tires = CarriganTire(tire_wear_array)
        elif tire_type == "Octoprime":
            tires = OctoprimeTire(tire_wear_array)

        return Car(engine, battery, tires)

    @staticmethod
    def create_rorschach(current_mileage, last_service_mileage, last_service_date, tire_type, tire_wear_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        
        if tire_type == "Carrigan":
            tires = CarriganTire(tire_wear_array)
        elif tire_type == "Octoprime":
            tires = OctoprimeTire(tire_wear_array)

        return Car(engine, battery, tires)

    @staticmethod
    def create_thovex(current_mileage, last_service_mileage, last_service_date, tire_type, tire_wear_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        
        if tire_type == "Carrigan":
            tires = CarriganTire(tire_wear_array)
        elif tire_type == "Octoprime":
            tires = OctoprimeTire(tire_wear_array)

        return Car(engine, battery, tires)
