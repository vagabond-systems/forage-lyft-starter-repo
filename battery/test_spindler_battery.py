import unittest
from spindler_battery import SpindlerBattery
from datetime import datetime

class TestSpindler(unittest.TestCase):
    def test_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()