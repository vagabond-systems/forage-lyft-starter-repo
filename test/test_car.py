import unittest
from datetime import datetime

from battery import SpindlerBattery
from engine import CapuletEngine
from car import Car


class TestCarFactory(unittest.TestCase):
    def test_is_instance_of_car(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(today, last_service_date)

        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery)
        self.assertIsInstance(car, Car)


if __name__ == '__main__':
    unittest.main()