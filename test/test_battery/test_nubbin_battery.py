import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_replaced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)

        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_replaced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())