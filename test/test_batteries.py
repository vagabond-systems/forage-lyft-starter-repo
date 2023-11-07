import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        current_date = date.fromisoformat("2023-11-04")
        last_service_date = date.fromisoformat("2018-11-04")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_does_not_needs_service(self):
        current_date = date.fromisoformat("2023-11-04")
        last_service_date = date.fromisoformat("2022-11-04")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        current_date = date.fromisoformat("2023-11-04")
        last_service_date = date.fromisoformat("2015-11-04")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_does_not_needs_service(self):
        current_date = date.fromisoformat("2023-11-04")
        last_service_date = date.fromisoformat("2022-11-04")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())