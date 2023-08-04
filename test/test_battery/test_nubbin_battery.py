import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-07-15")
        last_service_date = date.fromisoformat("2019-05-15")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-07-15")
        last_service_date = date.fromisoformat("2022-05-15")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
