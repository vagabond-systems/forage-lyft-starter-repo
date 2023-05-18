import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class Test_Nubbin(unittest.TestCase):
    def test_needs_service(self):
        battery = NubbinBattery(datetime.today().date().replace(year=2017), datetime.today().date())
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        battery = NubbinBattery(datetime.today().date(), datetime.today().date())
        self.assertFalse(battery.needs_service())

class Test_Spindler(unittest.TestCase):
    def test_needs_service(self):
        battery = SpindlerBattery(datetime.today().date().replace(year=2020), datetime.today().date())
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        battery = SpindlerBattery(datetime.today().date(), datetime.today().date())
        self.assertFalse(battery.needs_service())