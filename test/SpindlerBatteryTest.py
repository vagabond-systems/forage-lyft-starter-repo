import unittest
from datetime import datetime
from battery.spindlerBattery import SpindlerBattery


class SpindlerBatteryTest(unittest.TestCase):
    def test_battery_should_be_served(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_served(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

