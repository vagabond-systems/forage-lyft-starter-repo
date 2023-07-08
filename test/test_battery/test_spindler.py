import unittest

from datetime import datetime
from battery.spindler_battery import SpindlerBattery


class TestSpindler(unittest.TestCase):
    def test_spindler_battery_should_serviced_true(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        battery = SpindlerBattery(last_service_date)
        self.assertTrue(battery.battery_should_be_serviced())

    def test_spindler_battery_should_serviced_false(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        battery = SpindlerBattery(last_service_date)
        self.assertFalse(battery.battery_should_be_serviced())


if __name__ == "__main__":
    unittest.main()