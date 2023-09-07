import unittest
from datetime import datetime

from battery.battery_type.nubbin_battery import NubbinBattery
from battery.battery_type.splinder_battery import SplinderBattery


class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = NubbinBattery(today, last_service_date)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = NubbinBattery(today, last_service_date)
        self.assertFalse(car.needs_service())




class TestSplinder(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = SplinderBattery(today, last_service_date)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        car = SplinderBattery(today, last_service_date)
        self.assertFalse(car.needs_service())