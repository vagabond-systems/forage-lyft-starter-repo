import unittest
from datetime import date

from battery.spindler_battery import Spindler

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2018-02-20")
        battery = Spindler(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-03-13")
        battery = Spindler(current_date, last_service_date)
        self.assertFalse(battery.needs_service())