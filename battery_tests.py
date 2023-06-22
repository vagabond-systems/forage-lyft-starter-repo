import unittest
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from datetime import datetime


class TestBattery(unittest.TestCase):

    def test_nubbin_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 5)

        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_nubbin_does_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 3)
        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

    def test_spindler_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 3)
        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_spindler_does_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 1)
        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
