import unittest
from datetime import datetime
from battery.splinder_battery import SplinderBattery

class TestSplinderBattery(unittest.TestCase):
    def test_battery_should_be_replaced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)

        battery = SplinderBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_replaced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        battery = SplinderBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())