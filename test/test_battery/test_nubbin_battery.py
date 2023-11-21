
import unittest
from datetime import datetime, timedelta
from battery.battery import Battery
from battery.nubbin_battery import NubbinBattery
from utils import add_years_to_date


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        """ Set up the current date and last service date"""

        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2018, 1, 1)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        result = nubbin_battery.needs_service()
        self.assertTrue(result)

    def test_needs_service_false(self):
        """ Set up the current date and last service date"""
        current_date = datetime(2020, 1, 1)
        last_service_date = datetime(2022, 1, 1)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        result = nubbin_battery.needs_service()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
