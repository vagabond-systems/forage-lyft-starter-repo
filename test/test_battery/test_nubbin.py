import unittest

from datetime import datetime
from battery.nubbin_battery import NubbinBattery


class TestNubbin(unittest.TestCase):
    def test_nubbin_battery_should_serviced_true(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(last_service_date)
        self.assertTrue(battery.battery_should_be_serviced())

    def test_nubbin_battery_should_serviced_false(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = NubbinBattery(last_service_date)
        self.assertFalse(battery.battery_should_be_serviced())



if __name__ == "__main__":
    unittest.main()