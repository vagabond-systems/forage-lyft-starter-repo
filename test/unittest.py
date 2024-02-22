import unittest
from datetime import date

class TestEngine(unittest.TestCase):
    def test_needs_service(self):
        # Test Engine needs_service method
        engine = Engine(last_service_mileage=10000, current_mileage=12000)
        self.assertTrue(engine.needs_service())  # Assuming the engine needs service

    # Add more test cases for Engine as needed

class TestBattery(unittest.TestCase):
    def test_needs_service(self):
        # Test Battery needs_service method
        battery = Battery(last_service_date=date(2023, 1, 1), current_date=date(2024, 1, 1))
        self.assertTrue(battery.needs_service())  # Assuming the battery needs service

    # Add more test cases for Battery as needed

class TestCar(unittest.TestCase):
    def test_needs_service(self):
        # Test Car needs_service method
        engine = WilloughbyEngine(last_service_mileage=10000, current_mileage=12000)
        battery = NubbinBattery(last_service_date=date(2023, 1, 1), current_date=date(2024, 1, 1))
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())  # Assuming either engine or battery needs service

    # Add more test cases for Car as needed

class TestCarFactory(unittest.TestCase):
    def test_create_calliope(self):
        # Test CarFactory create_calliope method
        car = CarFactory.create_calliope(current_date=date(2024, 1, 1), last_service_date=date(2023, 1, 1), current_mileage=12000, last_service_mileage=10000)
        self.assertIsInstance(car, Car)

    # Add more test cases for CarFactory as needed

if __name__ == '__main__':
    unittest.main()