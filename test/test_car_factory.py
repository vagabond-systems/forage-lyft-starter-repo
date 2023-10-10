import unittest
from datetime import date
from car_Factory import CarFactory
from car_Module import Car 
from car_Module.components.battery import NubbinBattery, SpindlerBattery
from car_Module.components.engine import CapuletEngine, SternmanEngine, WilloughbyEngine

class TestCarFactory(unittest.TestCase):
    def test_create_calliope(self):
        car = CarFactory.create_calliope(date(2023, 10, 10), date(2022, 10, 10), 5000, 2500)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)

    def test_create_glissade(self):
        car = CarFactory.create_glissade(date(2023, 10, 10), date(2022, 10, 10), 5000, 2500)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)

    def test_create_palindrome(self):
        car = CarFactory.create_palindrome(date(2023, 10, 10), date(2022, 10, 10), True)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, SternmanEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)

    def test_create_rorschach(self):
        car = CarFactory.create_rorschach(date(2023, 10, 10), date(2022, 10, 10), 5000, 2500)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, NubbinBattery)

    def test_create_thovex(self):
        car = CarFactory.create_thovex(date(2023, 10, 10), date(2022, 10, 10), 5000, 2500)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, NubbinBattery)

if __name__ == '__main__':
    unittest.main()