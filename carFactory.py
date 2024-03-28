from car import Car
from engine import *
from battery import *
from datetime import date

class CarFactory():

    def create_calliope(self, current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int):

        self.engine = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = SpindleBattery(current_date, last_service_date)
        self.car = Car(self.engine, self.car)

        return self.car
    
    def create_glissade(self, current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int):

        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = SpindleBattery(current_date, last_service_date)
        self.car = Car(self.engine, self.car)

        return self.car
    
    def create_palindrome(self, current_date:date, last_service_date:date, warning_light_is_on:bool):

        self.engine = SternmanEngine(warning_light_is_on)
        self.battery = SpindleBattery(current_date, last_service_date)
        self.car = Car(self.engine, self.car)

        return self.car
    
    def create_rorschach(self, current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int):

        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = NubbinBattery(current_date, last_service_date)
        self.car = Car(self.engine, self.car)

        return self.car
    
    def create_thovex(self, current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int):

        self.engine = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = NubbinBattery(current_date, last_service_date)
        self.car = Car(self.engine, self.car)

        return self.car
    
