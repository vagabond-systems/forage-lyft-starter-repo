import unittest
from datetime import datetime

from battery import SpindlerBattery, NubinBattery
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from car import Car


class TestCarFactory(unittest.TestCase):
    def test_create_calliope(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(today, last_service_date)

        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery)
        self.assertIsInstance(car, Car)

    def test_create_glissade(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(today, last_service_date)

        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery)
        self.assertIsInstance(car, Car)

    def test_create_palindrome(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(today, last_service_date)

        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)

        car = Car(engine, battery)
        self.assertIsInstance(car, Car)

    def test_create_rorschach(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubinBattery(today, last_service_date)

        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery)
        self.assertIsInstance(car, Car)

    def test_create_thovex(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubinBattery(today, last_service_date)

        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery)
        self.assertIsInstance(car, Car)


if __name__ == '__main__':
    unittest.main()