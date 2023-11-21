import unittest
from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery


class TestCar(unittest.TestCase):
    def test_needs_service_true(self):
        """Create a Car instance with components that need services"""
        capulet_engine = CapuletEngine(current_mileage=35000,
                                       last_service_mileage=20000)
        spindler_battery = SpindlerBattery(current_date=datetime(2023, 1, 1),
                                           last_service_date=datetime
                                           (2020, 1, 1))
        car = Car(engine=capulet_engine, battery=spindler_battery)
        result = car.needs_service()
        self.assertTrue(result)

    def test_needs_service_false(self):
        """Create a Car instance with components that don't need service"""
        capulet_engine = CapuletEngine(current_mileage=25000,
                                       last_service_mileage=20000)
        spindler_battery = SpindlerBattery(current_date=datetime(2023, 1, 1),
                                           last_service_date=datetime
                                           (2022, 1, 1))
        car = Car(engine=capulet_engine, battery=spindler_battery)
        result = car.needs_service()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
