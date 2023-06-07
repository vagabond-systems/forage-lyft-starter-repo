from car import Car
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine

class CarFactory:
    @staticmethod
    def create_calliope(tire_wear):
        car = Car()
        car.add_engine(WilloughbyEngine())
        car.add_battery()
        car.add_tires(tire_wear, threshold=0.9)  # Carrigan tires
        return car

    @staticmethod
    def create_glissade(tire_wear):
        car = Car()
        car.add_engine(SternmanEngine())
        car.add_battery()
        car.add_tires(tire_wear, threshold=0.9)  # Carrigan tires
        return car

    @staticmethod
    def create_palindrome(tire_wear):
        car = Car()
        car.add_engine(SternmanEngine())
        car.add_battery()
        car.add_tires(tire_wear, threshold=3)  # Octoprime tires
        return car

    @staticmethod
    def create_rorschach(tire_wear):
        car = Car()
        car.add_engine(SternmanEngine())
        car.add_battery()
        car.add_tires(tire_wear, threshold=3)  # Octoprime tires
        return car

    @staticmethod
    def create_thovex(tire_wear):
        car = Car()
        car.add_engine(SternmanEngine())
        car.add_battery()
        car.add_tires(tire_wear, threshold=3)  # Octoprime tires
        return car
