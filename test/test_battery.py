import unittest
from datetime import datetime

import sys
sys.path.append('/Volumes/sourcecode/forage-lyft-starter-repo')

from battery import SpindlerBattery, NubinBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(today, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        battery = SpindlerBattery(today, last_service_date)

        self.assertFalse(battery.needs_service())

class TestNubinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubinBattery(today, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        battery = NubinBattery(today, last_service_date)

        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()